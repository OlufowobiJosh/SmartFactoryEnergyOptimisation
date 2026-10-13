"""Reproducible demonstration using synthetic factory data only."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.metrics import silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_factory_energy.csv"

def main():
    df = pd.read_csv(DATA, parse_dates=["date"])
    assert df["date"].is_unique
    print("Synthetic data shape:", df.shape)
    print("Missing values:\n", df.isna().sum())
    print("Energy correlations:\n", df.select_dtypes("number").corr()["total_energy_kwh"].sort_values(ascending=False))
    features = ["ambient_temperature_c", "ambient_humidity_pct", "finished_goods_units", "machine_runtime_hours", "cooling_energy_kwh", "compressor_energy_kwh", "injection_energy_kwh"]
    x = make_pipeline(SimpleImputer(strategy="median"), StandardScaler()).fit_transform(df[features])
    results = {}
    for k in (2, 3, 4, 5):
        labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(x)
        results[k] = silhouette_score(x, labels)
    best_k = max(results, key=results.get)
    labels = KMeans(n_clusters=best_k, n_init=10, random_state=42).fit_predict(x)
    print("Synthetic-data silhouette scores:", {k: round(v, 3) for k, v in results.items()})
    print("Best k on synthetic data:", best_k)
    print("Cluster profiles (synthetic data):\n", df.assign(cluster=labels).groupby("cluster")[["total_energy_kwh", "finished_goods_units", "cooling_energy_kwh"]].mean().round(1))
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["date"], df["total_energy_kwh"])
    ax.set(title="Synthetic factory energy consumption", xlabel="Date", ylabel="Energy (kWh)")
    fig.tight_layout()
    out = ROOT / "synthetic_energy_trend.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    coords = PCA(n_components=2).fit_transform(x)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(coords[:, 0], coords[:, 1], c=labels, cmap="viridis", s=18)
    ax.set(title="Operating-mode clusters (synthetic data)", xlabel="PC1", ylabel="PC2")
    fig.tight_layout()
    fig.savefig(ROOT / "synthetic_clusters.png", dpi=150)
    plt.close(fig)

if __name__ == "__main__":
    main()

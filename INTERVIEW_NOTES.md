# Interview talking points — original MSc final-year project

**30-second explanation:** “For my MSc final-year project at the University of Hull, I investigated factors associated with energy consumption in a smart manufacturing environment. I combined energy, production and environmental data, explored correlations and time patterns, and compared unsupervised approaches to identify operating modes. The academic report reported an Autoencoder + K-Means silhouette score of 0.6135. I translated the analysis into recommendations to investigate cooling systems and production-related energy demand.”

**Business value:** Helps prioritise where to monitor and investigate energy efficiency; it does **not** demonstrate that cost savings were achieved.

**Why unsupervised learning?** There were no predefined labels for efficient versus inefficient operating modes. Clustering explored patterns without such labels.

**Why scaling?** Temperature, production units and kWh are on different scales; unscaled K-Means can overemphasise larger-number variables.

**What does silhouette 0.6135 mean?** A measure of within-cluster cohesion and between-cluster separation, with higher generally better. It does not prove real operational efficiency.

**Key limitation:** Observational correlations do not establish causality. The academic report has a three-versus-four-cluster inconsistency in figure captions; confirm from the original code and results before describing the exact cluster count. The original notebook provided here mostly covers exploratory plots; it does not contain the full modelling workflow reported in the academic report.

**Confidentiality:** Discuss methodology at a high level. Do not share original factory files, proprietary machine IDs, raw screenshots, or company-specific results without permission. The public GitHub demo uses synthetic data.

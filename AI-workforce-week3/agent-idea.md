## Data Guardian Agent (*A Copilot Agent Idea*)

**Data Guardian Agent** exists to solve a quiet but costly problem: data breaks not because code is wrong, but because meaning is lost.  
It helps data engineers catch schema misuse, contract violations, and risky transformations *before* they reach production or confuse downstream users.

This agent is for **data engineers and analytics engineers** who work daily with evolving schemas, complex SQL, dbt models, or Spark jobs—and who care about trust in the data they ship.  
It’s especially valuable for teams moving fast, where reviews are short and context is easy to miss.

Data Guardian understands your schemas, column definitions, data contracts, and dependencies, and uses that context when reviewing transformations.  
It can answer questions like: *“Does this change break downstream models?”*, *“Is this column being used outside its contract?”*, or *“Which datasets are affected if I modify this table?”*  

It can review SQL or transformation logic and flag issues like unsafe joins, missing filters, contract violations, or mismatches between intent and implementation.  
It can also explain *why* something is risky, not just that it is.

Beyond reviews, the agent helps with clarity.  
You can ask it to explain a dataset in plain language, trace data flow end‑to‑end, or summarize what changed between versions of a model.  

At its core, Data Guardian isn’t about control or policing. It is about **protecting meaning, reducing surprises, and helping engineers sleep better after deployments**.
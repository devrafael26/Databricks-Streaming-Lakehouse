CREATE OR REFRESH MATERIALIZED VIEW workspace.gold.state_ranking
AS

SELECT

    state,

    COUNT(*) AS total_orders,

    SUM(orderunits) AS total_units,

    ROUND(AVG(orderunits), 0) AS avg_units

FROM workspace.silver.orders_silver

GROUP BY state

ORDER BY total_orders DESC;
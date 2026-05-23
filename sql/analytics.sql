SELECT
    Tid,
    AVG(value) AS avg_index_value
FROM ssb_construction_cost_index
WHERE ContentsCode = 'Construction cost index'
GROUP BY Tid
ORDER BY Tid DESC;
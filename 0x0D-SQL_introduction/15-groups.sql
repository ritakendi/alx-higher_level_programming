-- Groups up scores and displays totals of multiple equal scores
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;

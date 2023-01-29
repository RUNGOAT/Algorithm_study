SELECT P1.ID, P1.NAME, P1.HOST_ID
FROM PLACES P1 JOIN (
                SELECT HOST_ID
                FROM PLACES
                GROUP BY HOST_ID
                HAVING COUNT(ID) > 1
                ) P2
USING (HOST_ID)
ORDER BY P1.ID;
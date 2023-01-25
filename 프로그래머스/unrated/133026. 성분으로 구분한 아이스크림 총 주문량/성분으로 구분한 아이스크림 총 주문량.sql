SELECT I.INGREDIENT_TYPE, SUM(F.TOT) AS TOTAL_ORDER
  FROM ICECREAM_INFO AS I
        LEFT JOIN
        (
            SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOT
              FROM FIRST_HALF
             GROUP BY FLAVOR
        ) AS F ON I.FLAVOR = F.FLAVOR
 GROUP BY I.INGREDIENT_TYPE
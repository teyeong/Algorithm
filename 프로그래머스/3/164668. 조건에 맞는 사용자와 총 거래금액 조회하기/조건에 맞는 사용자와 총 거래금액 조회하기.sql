SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD, USED_GOODS_USER
GROUP BY USER_ID, WRITER_ID, STATUS
HAVING WRITER_ID = USER_ID AND STATUS = "DONE" AND TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC;
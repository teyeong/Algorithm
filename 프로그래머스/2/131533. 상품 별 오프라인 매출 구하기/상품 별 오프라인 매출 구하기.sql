SELECT A.PRODUCT_CODE, A.PRICE * B.SALES_AMOUNT AS SALES FROM PRODUCT AS A
INNER JOIN (
    SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS SALES_AMOUNT FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) AS B ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY SALES DESC, A.PRODUCT_CODE ASC;
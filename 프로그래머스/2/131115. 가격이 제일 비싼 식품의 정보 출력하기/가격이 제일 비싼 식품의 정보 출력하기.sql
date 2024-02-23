SELECT A.PRODUCT_ID, A.PRODUCT_NAME, A.PRODUCT_CD, A.CATEGORY, A.PRICE FROM FOOD_PRODUCT AS A
INNER JOIN (
    SELECT PRODUCT_ID, MAX(PRICE) AS PRICE FROM FOOD_PRODUCT
) AS B ON A.PRICE = B.PRICE;
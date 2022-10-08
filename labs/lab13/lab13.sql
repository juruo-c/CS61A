.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price)
  FROM inventory
  GROUP BY item;


CREATE TABLE best_item AS 
  SELECT name AS item, MIN(MSRP / rating)
  FROM products 
  GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT best_item.item AS item, lowest_prices.store AS store
  FROM best_item, lowest_prices
  WHERE best_item.item = lowest_prices.item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)
  FROM shopping_list, stores
  WHERE stores.store = shopping_list.store;


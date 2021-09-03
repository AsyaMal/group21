1. Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и hd
SELECT model, speed, hd FROM PC WHERE price < 500;
===============
2. Найдите производителей принтеров. Вывести: maker
SELECT DISTINCT maker FROM Product WHERE type = 'printer';
===============
3. Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
SELECT model, ram, screen FROM Laptop WHERE price > 1000;
===============
4. Найдите все записи таблицы Printer для цветных принтеров.
SELECT * FROM Printer WHERE color = "y";
===============
5. Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
SELECT model, speed, hd FROM PC WHERE (cd = '12x' OR cd = '24x') AND price < 600;
===============
6. Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
SELECT DISTINCT Product.maker, Laptop.speed FROM Product JOIN Laptop ON Product.model = Laptop.model WHERE Laptop.hd >= 10;
===============
7. Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
SELECT PLP.model, price FROM (SELECT model, price FROM PC UNION SELECT model, price FROM Laptop UNION SELECT model, price FROM Printer) AS PLP JOIN Product ON PLP.model = Product.model WHERE Product.maker = "B";
===============
8. Найдите производителя, выпускающего ПК, но не ПК-блокноты.
SELECT DISTINCT maker FROM Product WHERE type = 'PC' AND maker NOT IN (SELECT maker FROM Product WHERE type = 'Laptop')
===============
9. Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
SELECT DISTINCT product.maker AS maker FROM product JOIN pc ON product.model = pc.model WHERE pc.speed >= 450
===============
10. Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
SELECT model, price FROM printer WHERE price = (SELECT MAX(price) FROM printer);
===============
11. Найдите среднюю скорость ПК.
SELECT AVG(speed) FROM PC;
===============
12. Найдите среднюю скорость ПК-блокнотов, цена которых превышает 1000 дол.
SELECT AVG(speed) FROM Laptop WHERE price > 1000;
===============
13. Найдите среднюю скорость ПК, выпущенных производителем A.
SELECT AVG(PC.speed) FROM PC JOIN Product ON PC.model = Product.model WHERE Product.maker = 'A';
===============
14. Найдите класс, имя и страну для кораблей из таблицы Ships, имеющих не менее 10 орудий.
SELECT Ships.class, Ships.name, Classes.country FROM Ships JOIN Classes ON Ships.class = Classes.class WHERE Classes.numGuns >= 10;
===============
15. Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
SELECT hd FROM PC GROUP BY hd HAVING COUNT(model) >= 2;
===============
16. Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i), Порядок вывода: модель с большим номером, модель с меньшим номером, скорость и RAM.
SELECT DISTINCT B.model AS model, A.model AS model, A.speed, A.ram FROM PC AS A, PC B WHERE A.speed = B.speed AND A.ram = B.ram and A.model < B.model; 
===============
17. Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК.Вывести: type, model, speed
SELECT DISTINCT P.type, L.model, L.speed FROM Product AS P JOIN Laptop AS L ON P.model = L.model WHERE L.speed < (SELECT MIN(PC.speed) FROM PC);
===============
18. Найдите производителей самых дешевых цветных принтеров. Вывести: maker, price
###SELECT DISTINCT P.maker, Pr.price FROM Product AS P JOIN Printer AS Pr ON P.model = Pr.model WHERE price = (SELECT MIN(price) FROM Pr WHERE color ='y') AND color = 'y';
===============
19. Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов.
Вывести: maker, средний размер экрана.
SELECT p.maker, AVG(l.screen) FROM product p JOIN laptop l ON p.model = l.model GROUP by p.maker;
===============
20. Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.
SELECT maker, COUNT(model) FROM product WHERE type = 'pc' GROUP BY maker HAVING COUNT (DISTINCT model) >= 3
===============
21. Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
Вывести: maker, максимальная цена.
SELECT p.maker, MAX(pc.price) FROM product p JOIN pc ON p.model = pc.model GROUP by p.maker;
===============
22. Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена.
SELECT speed, AVG(price) FROM pc WHERE speed > 600 GROUP BY speed;
===============
23. Найдите производителей, которые производили бы как ПК со скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц. Вывести: Maker
SELECT DISTINCT p.maker FROM product p JOIN pc ON p.model = pc.model WHERE pc.speed >= 750 AND maker IN (SELECT maker FROM product p JOIN Laptop l ON p.model = l.model WHERE l.speed >= 750);
===============
24. Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
SELECT model FROM (SELECT model, price FROM pc UNION SELECT model, price FROM Laptop UNION SELECT model, price FROM Printer) o WHERE price = (SELECT MAX(price) FROM (SELECT price FROM pc UNION SELECT price  FROM Laptop UNION  SELECT price FROM Printer) k)
===============
25. Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM. Вывести: Maker
SELECT DISTINCT maker FROM product WHERE model IN (SELECT model FROM pc WHERE ram = (SELECT MIN(ram) FROM pc) AND speed = (SELECT MAX(speed) FROM pc WHERE ram = (SELECT MIN(ram) FROM pc))) AND maker IN (SELECT maker FROM product WHERE type = 'printer');
===============
26. Найдите среднюю цену ПК и ПК-блокнотов, выпущенных производителем A (латинская буква). Вывести: одна общая средняя цена.
SELECT AVG(price) AS Avg_p FROM (SELECT model, price FROM pc UNION ALL SELECT model, price FROM laptop) AS price JOIN product p ON price.model = p.model WHERE p.maker = 'A' 
===============
27. Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и принтеры. Вывести: maker, средний размер HD.
SELECT p.maker, avg(pc.hd) as avg_hd from product p join pc on p.model = pc.model where p.maker in (select maker from product where type = 'printer') group by p.maker;
===============
28. Используя таблицу Product, определить количество производителей, выпускающих по одной модели.
SELECT COUNT(maker) AS Q FROM (SELECT DISTINCT maker
FROM product GROUP BY maker HAVING COUNT(model) = 1) AS prod
===============
29. В предположении, что приход и расход денег на каждом пункте приема фиксируется не чаще одного раза в день [т.е. первичный ключ (пункт, дата)], написать запрос с выходными данными (пункт, дата, приход, расход). Использовать таблицы Income_o и Outcome_o.
select i.point, i.date, inc, out from income_o i left join outcome_o o on i.point = o.point and i.date = o.date union select o.point, o.date, inc, out from income_o i right join outcome_o o on i.point = o.point and i.date = o.date
===============
30. В предположении, что приход и расход денег на каждом пункте приема фиксируется произвольное число раз (первичным ключом в таблицах является столбец code), требуется получить таблицу, в которой каждому пункту за каждую дату выполнения операций будет соответствовать одна строка.
Вывод: point, date, суммарный расход пункта за день (out), суммарный приход пункта за день (inc). Отсутствующие значения считать неопределенными (NULL).
SELECT point, date, SUM(sum_out), SUM(sum_inc)
FROM (SELECT point, date, SUM(inc) AS sum_inc, null AS sum_out FROM Income GROUP BY point, date UNION SELECT point, date, null AS sum_inc, SUM(out) AS sum_out from Outcome GROUP BY point, date ) AS t GROUP BY point, date ORDER BY point
===============













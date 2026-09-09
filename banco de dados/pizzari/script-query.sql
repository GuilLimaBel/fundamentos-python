SELECT COUNT(id) FROM pedidos;

SELECT CONCAT('R$', SUM(total))
FROM pedidos;

/*Quantos pedidos foram cancelados?*/
SELECT
    COUNT(id) FROM pedidos 
WHERE status = 'cancelado';

/*Mostrar os pedidos que foram cancelados*/
SELECT 
    status
    
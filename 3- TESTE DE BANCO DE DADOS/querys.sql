-- Query para encontrar as 10 operadoras com maiores despesas no último trimestre
SELECT operadoras.razao_social, SUM(eventos_sinistros.valor) AS total_despesas
FROM eventos_sinistros
JOIN operadoras ON eventos_sinistros.cnpj_operadora = operadoras.cnpj
WHERE eventos_sinistros.trimestre = QUARTER(NOW()) AND eventos_sinistros.ano = YEAR(NOW())
GROUP BY operadoras.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- Query para encontrar as 10 operadoras com maiores despesas no último ano
SELECT operadoras.razao_social, SUM(eventos_sinistros.valor) AS total_despesas
FROM eventos_sinistros
JOIN operadoras ON eventos_sinistros.cnpj_operadora = operadoras.cnpj
WHERE eventos_sinistros.ano = YEAR(NOW())
GROUP BY operadoras.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

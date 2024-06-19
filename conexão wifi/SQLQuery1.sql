use helenis

/*CREATE TABLE colaboradores (EDV int primary key, Names varchar(60), Age int, Salary float);*/

--INSERT INTO dbo.colaboradores( EDV, Names, Age, Salary) values (1, 'José', 52, 10000.6);
--INSERT INTO dbo.colaboradores( EDV, Names, Age, Salary) values (2, 'Ana Maria', 22, 588967.6);
--INSERT INTO dbo.colaboradores( EDV, Names, Age, Salary) values (3, 'Cláudia', 54, 10000.95);
--INSERT INTO dbo.colaboradores( EDV, Names, Age, Salary) values (4, 'Cristian', 2, 10.6);

-- Com * seleciona toda a tabela
--SELECT * from dbo.colaboradores;

-- Seleciona apena uma 
--SELECT Salary from dbo.colaboradores;

-- Seleciona coluna uma específica
--SELECT Names, Age from dbo.colaboradores;

-- Filtro
--SELECT Names, Age from dbo.colaboradores WHERE Age<30;

-- Organiza por tamanho
--SELECT Names, Salary FROM dbo.colaboradores ORDER BY Salary;

-- Atualiza os dados
--UPDATE dbo.colaboradores SET Names='Helena' WHERE EDV=2;

-- Deletar dado
--DELETE FROM dbo.colaboradores WHERE EDV=1;

--Delete a tabela
--DROP TABLE dbo.colaboradores;
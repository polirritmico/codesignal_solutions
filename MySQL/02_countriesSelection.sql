CREATE PROCEDURE solution()
BEGIN
    SELECT * FROM countries WHERE continent LIKE "%Africa%";
END

-- Crea una tabella dove conta, per ogni exam, quanti errori ci sono di una specifica class
SELECT exam, class, COUNT(*) AS numb_of_errors
FROM last_croudy_errors_class_csv
GROUP BY exam, class;

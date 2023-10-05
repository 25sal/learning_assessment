-- conta, per ogni exam, quanti errori ci sono di una specifica class
SELECT exam, class, COUNT(*) AS numb_of_errors
FROM last_croudy_errors_class_csv
GROUP BY exam, class;

-- Con questa query è possibile capire quante volte uno studente ha consegnato un compito con errori
select count(distinct session) as cnt, studentid
from last_error_with_student
group by studentid
order by cnt desc;

-- serve a vedere quante  volte uno studente ha compilato un particolare compito
select count(id) as cnt, exam, compilations.datetime
from compilations
group by exam
order by cnt desc;

-- mi dice quante prove, differenti, sono presenti nel db
select *
from (select count(distinct session) as cnt, studentid
      from last_error_with_student
      group by studentid
      order by cnt desc)
where cnt > 1;

-- conta, per ogni compilazione, quanti errori ci sono di una specifica class(in questo caso label)
SELECT exam,
       compilationid,
       label,
       COUNT(*)
           AS numb_of_errors
FROM all_logs_class
WHERE type == 'error'
GROUP BY compilationid, exam, label

-- uguale a quella di sopra ma con un mapping per trasformare la label nella classe di ErrorTopics
SELECT exam,
       compilationid,
       CASE
           WHEN label = 'declaration' THEN 0
           WHEN label = 'conflict' THEN 1
           WHEN label = 'incompatibility' THEN 2
           WHEN label = 'assignment' THEN 3
           WHEN label = 'initialization' THEN 4
           WHEN label = 'parameters' THEN 5
           WHEN label = 'syntax' THEN 6
           WHEN label = 'array/struct' THEN 7
           ELSE label -- If none of the enum values match, keep the original label
           END  AS class,
       COUNT(*) AS numb_of_errors
FROM all_logs_class
WHERE type = 'error'
GROUP BY compilationid, exam, class;
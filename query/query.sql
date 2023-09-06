-- Crea una tabella dove conta, per ogni exam, quanti errori ci sono di una specifica class
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

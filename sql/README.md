# MySQL


## Notes on how I setup the repo
```bash
juan@Juans-MacBook-Air ~/src/MySQL
$ git add README.md

juan@Juans-MacBook-Air ~/src/MySQL
$ git commit -m "First commit"
[master (root-commit) 1809af1] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

juan@Juans-MacBook-Air ~/src/MySQL
$ git remote add origin https://github.com/JJDLTorre/MySQL.git

juan@Juans-MacBook-Air ~/src/MySQL
$ git push -u origin master
Counting objects: 3, done.
Writing objects: 100% (3/3), 226 bytes | 226.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/JJDLTorre/MySQL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

## How to verify that MySQL has the correct character set
```SQL
SHOW VARIABLES LIKE 'character_set%';
-- # Variable_name, Value
-- 'character_set_client', 'utf8'
-- 'character_set_connection', 'utf8'
-- 'character_set_database', 'latin1'
-- 'character_set_filesystem', 'binary'
-- 'character_set_results', 'utf8'
-- 'character_set_server', 'latin1'
-- 'character_set_system', 'utf8'
-- 'character_sets_dir', '/usr/share/mysql/charsets/'

# After vi /etc/my.cnf: character-set-server=utf8
-- # Variable_name, Value
-- 'character_set_client', 'utf8'
-- 'character_set_connection', 'utf8'
-- 'character_set_database', 'latin1'
-- 'character_set_filesystem', 'binary'
-- 'character_set_results', 'utf8'
-- 'character_set_server', 'utf8'
-- 'character_set_system', 'utf8'
-- 'character_sets_dir', '/usr/share/mysql/charsets/'

-- ALTER DATABASE myDatabase CHARACTER SET utf8;
-- commit;
SHOW VARIABLES LIKE 'character_set%';
-- # Variable_name, Value
-- 'character_set_client', 'utf8'
-- 'character_set_connection', 'utf8'
-- 'character_set_database', 'utf8'
-- 'character_set_filesystem', 'binary'
-- 'character_set_results', 'utf8'
-- 'character_set_server', 'utf8'
-- 'character_set_system', 'utf8'
-- 'character_sets_dir', '/usr/share/mysql/charsets/'
```

## Example of using WITH and UNION
```SQL
-- Get course and instructor surveys order by term_code and (course then instructor survey)
with emplid_and_college_code_survey (emplid, college_code, term_code, FULL_FILE_NAME) as
(
    select cs.emplid, cs.college_code, REGEXP_REPLACE(FULL_FILE_NAME, '.*-(\d{4})_?\w*\].*', '\1') as term_code, FULL_FILE_NAME from course_cc_survey cs
    where
    (cs.emplid || '_' || cs.college_code) in
    (
        select emplid_to_alias.emplid || '_' || ccta.COLLEGE_CODE
        from
        (
            select REGEXP_REPLACE(column_value, '(.*)-.*', '\1') as emplid, REGEXP_REPLACE(column_value, '.*-(.*)', '\1') as collage_alias 
            from
            table(sys.odcivarchar2list
            -- This is the list of id and college_alias given to us
            ('000012345-CAED',...')
            )
        ) emplid_to_alias
        inner join COLLEGE_CODE_TO_ALIAS ccta on ccta.college_alias = emplid_to_alias.collage_alias
    )
)
 
select * from (
    select e01.emplid as emplid, e01.college_code as college_code, e01.term_code as term_code,
        e01.full_file_name as full_file_name , '1' as order_num
    from emplid_and_college_code_survey e01
     
    union
     
    select is01.emplid as emplid, is01.college_code  as college_code,
        regexp_replace(is01.survey_year, '(\d)\d(\d\d)', '\1\2') || (case when is01.term='Winter' then '2' when is01.term='Spring' then '4' when is01.term='Summer' then '6' when is01.term='Fall' then '8' end) as term_code,
        is01.full_file_name as full_file_name, '2' as order_num
    from instructor_cc_survey is01
    inner join emplid_and_college_code_survey e on (is01.emplid || '_' || is01.college_code) = (e.emplid || '_' || e.college_code)
) order_files
order by order_files.emplid, order_files.college_code, order_files.term_code, order_files.order_num
;
```

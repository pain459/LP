create table customer
(
  id        integer primary key,
  name      text not null,
  comment   text
);


with customer_json (doc) as (
   values
    ('[
      {
        "id": 23635,
        "name": "Jerry Green",
        "comment": "Imported from facebook."
      },
      {
        "id": 23636,
        "name": "John Wayne",
        "comment": "Imported from facebook."
      }
    ]'::json)
)
insert into customer (id, name, comment)
select p.*
from customer_json l
  cross join lateral json_populate_recordset(null::customer, doc) as p
on conflict (id) do update
  set name = excluded.name,
      comment = excluded.comment;

-- https://stackoverflow.com/questions/39224382/how-can-i-import-a-json-file-into-postgresql
-- https://kb.objectrocket.com/postgresql/insert-json-data-into-postgresql-using-python-part-1-1247
-- https://kb.objectrocket.com/postgresql/insert-json-data-into-postgresql-using-python-part-2-1248

create database mobile;
\c mobile;
create table operateur(
    id_operateur Integer primary key,
    nom varchar(100)
);
create table phone(
    id Integer,
    id_operateur Integer references operateur(id_operateur),
    nom varchar(100)
);
insert into operateur values(1,'telma');
insert into operateur values(2,'airtel');
insert into operateur values(3,'orange');
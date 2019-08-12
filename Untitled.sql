mysql -h mirroring-demo-source.cluster-cnauspxugnzt.ap-northeast-1.rds.amazonaws.com -u song -p

create table sample_table(
   sample_id INT NOT NULL AUTO_INCREMENT,
   sample_field VARCHAR(100) NOT NULL,
   PRIMARY KEY ( sample_id )
);

use database sample_database;

insert into sample_table (sample_field) values ('881014-5123456');
insert into smoothies.public.orders(ingredients)
values ('Cantaloupe Guava Jackfruit Elderberries Figs ');

select * from smoothies.public.orders;

truncate table smoothies.public.orders;

alter table SMOOTHIES.PUBLIC.ORDERS ADD column ORDER_FILLED BOOLEAN DEFAULT FALSE;


       update smoothies.public.orders
       set order_filled = true
       where name_on_order is null;


insert into smoothies.public.orders(ingredients,NAME_ON_ORDER) values ('Dragon Fruit Honeydew Guava Apples Kiwi','MellyMel');



truncate table SMOOTHIES.PUBLIC.ORDERS;

alter table SMOOTHIES.PUBLIC.ORDERS
add column order_uid integer --adds the column
default smoothies.public.order_seq.nextval --sets the value of the column to sequence
constraint order_uid unique enforced; --makes sure there is always a unique value in the column



og_dataset = session.table("smoothies.public.orders")
    edited_dataset = session.create_dataframe(editable_df)
    og_dataset.merge(edited_dataset
                     , (og_dataset['ORDER_UID'] == edited_dataset['ORDER_UID'])
                     , [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]


                    );


select * from ORDERS;
alter table fruit_options add column SEARCH_ON TEXT;

-- copy name to seed the columns - then we can just edit the problem rows
update fruit_options
set search_on = SEARCH_ON;

select * from fruit_options;

update fruit_options
set search_on = 'Apple'
where SEARCH_ON = 'Apples';

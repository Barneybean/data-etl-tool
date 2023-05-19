-- create a dwh.membership table that match the output columns from the etl.py with primary key using customer_id
-- columns 'customer_id', 'first_name', 'last_name', 'original_customer_id', 'dob','company_name','last_active','score','member_since','state', 'source_org', 'created_at','updated_at', 'deleted_at'
CREATE TABLE IF NOT EXISTS public.membership
(
    customer_id varchar(255) NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    original_customer_id varchar(255),
    dob date,
    company_name varchar(255),
    last_active date,
    score numeric,
    member_since numeric,
    state varchar(255),
    source_org varchar(255),
    created_at timestamptz,
    updated_at timestamptz,
    deleted_at timestamptz,
    CONSTRAINT membership_pkey PRIMARY KEY (customer_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.membership
    OWNER to postgres;
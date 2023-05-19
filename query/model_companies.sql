-- select * from dwh.membership
CREATE TABLE IF NOT EXISTS public.companies
(
    id varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    created_at timestamptz,
    updated_at timestamptz,
    deleted_at timestamptz,
    CONSTRAINT companies_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.companies
    OWNER to postgres;
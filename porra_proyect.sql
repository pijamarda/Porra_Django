--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO zeneke;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO zeneke;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO zeneke;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO zeneke;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO zeneke;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO zeneke;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO zeneke;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO zeneke;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO zeneke;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO zeneke;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO zeneke;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO zeneke;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO zeneke;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO zeneke;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO zeneke;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO zeneke;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO zeneke;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO zeneke;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO zeneke;

--
-- Name: mundial2014_equipo; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE mundial2014_equipo (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    name character varying(200) NOT NULL,
    flag character varying(200) NOT NULL,
    equipo_id integer NOT NULL,
    grupo_id integer NOT NULL
);


ALTER TABLE public.mundial2014_equipo OWNER TO zeneke;

--
-- Name: mundial2014_equipo_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE mundial2014_equipo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mundial2014_equipo_id_seq OWNER TO zeneke;

--
-- Name: mundial2014_equipo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE mundial2014_equipo_id_seq OWNED BY mundial2014_equipo.id;


--
-- Name: mundial2014_grupo; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE mundial2014_grupo (
    id integer NOT NULL,
    grupo_id integer NOT NULL,
    nombre character varying(200) NOT NULL
);


ALTER TABLE public.mundial2014_grupo OWNER TO zeneke;

--
-- Name: mundial2014_grupo_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE mundial2014_grupo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mundial2014_grupo_id_seq OWNER TO zeneke;

--
-- Name: mundial2014_grupo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE mundial2014_grupo_id_seq OWNED BY mundial2014_grupo.id;


--
-- Name: mundial2014_partido; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE mundial2014_partido (
    id integer NOT NULL,
    partido_id integer NOT NULL,
    usuario_id integer NOT NULL,
    local integer NOT NULL,
    local_id integer NOT NULL,
    visitante integer NOT NULL,
    visitante_id integer NOT NULL
);


ALTER TABLE public.mundial2014_partido OWNER TO zeneke;

--
-- Name: mundial2014_partido_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE mundial2014_partido_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mundial2014_partido_id_seq OWNER TO zeneke;

--
-- Name: mundial2014_partido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE mundial2014_partido_id_seq OWNED BY mundial2014_partido.id;


--
-- Name: mundial2014_rank; Type: TABLE; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE TABLE mundial2014_rank (
    id integer NOT NULL,
    puntos integer NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.mundial2014_rank OWNER TO zeneke;

--
-- Name: mundial2014_rank_id_seq; Type: SEQUENCE; Schema: public; Owner: zeneke
--

CREATE SEQUENCE mundial2014_rank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mundial2014_rank_id_seq OWNER TO zeneke;

--
-- Name: mundial2014_rank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: zeneke
--

ALTER SEQUENCE mundial2014_rank_id_seq OWNED BY mundial2014_rank.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_equipo ALTER COLUMN id SET DEFAULT nextval('mundial2014_equipo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_grupo ALTER COLUMN id SET DEFAULT nextval('mundial2014_grupo_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_partido ALTER COLUMN id SET DEFAULT nextval('mundial2014_partido_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_rank ALTER COLUMN id SET DEFAULT nextval('mundial2014_rank_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add partido	7	add_partido
20	Can change partido	7	change_partido
21	Can delete partido	7	delete_partido
22	Can add equipo	8	add_equipo
23	Can change equipo	8	change_equipo
24	Can delete equipo	8	delete_equipo
25	Can add rank	9	add_rank
26	Can change rank	9	change_rank
27	Can delete rank	9	delete_rank
28	Can add grupo	10	add_grupo
29	Can change grupo	10	change_grupo
30	Can delete grupo	10	delete_grupo
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_permission_id_seq', 30, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$12000$zC8VixNiqJ3i$xi/cTEqyQu3H8rSBOQMfMO7pKZ+cVtWkF+CFfXnidzQ=	2014-09-18 15:49:23.448993+02	f	agormaz				f	t	2014-09-18 15:49:23.449105+02
12	pbkdf2_sha256$12000$pn745G0YB0lV$p1i8QgN5zJrKpUwnwHRd41eJX+Aw2E+2+UwxR06Jegw=	2014-09-22 14:17:48.25936+02	f	as				f	t	2014-09-22 14:17:48.259419+02
13	pbkdf2_sha256$12000$oxacgZxtzX2E$zpeTMcvTr8n6zuyXUT2FQayOnCgN5mrkDdT2qUXwXVE=	2014-09-22 14:18:04.983597+02	f	we				f	t	2014-09-22 14:18:04.983649+02
17	pbkdf2_sha256$12000$YvbQeaf1AxTv$ZxJ1wR7TCEBCmk73ub8k3riEvJ286iqmLp8BwvAnPKA=	2014-09-22 16:55:04.635677+02	f	random				f	t	2014-09-22 16:55:04.635733+02
18	pbkdf2_sha256$12000$riQKik3hKhbJ$2LzheKL7o3G0innpC0eLXfxQl3ZW2QZPDCV5Kkp1xHc=	2014-10-15 17:46:11.61588+02	f	hola				f	t	2014-10-15 17:46:11.615944+02
2	pbkdf2_sha256$12000$3CmFoAj7Tqkn$TSrgsOZ5EOAidb3lE02QHtTMNATI6HWqSbu2INqH3I0=	2014-10-16 17:57:32.737323+02	f	fgimenez				f	t	2014-09-18 12:52:58.954764+02
19	pbkdf2_sha256$12000$8GYpcWAqFCF7$7hX1Qpb1ZN8eRttap7q40zf5JrJPEaZmYYGkL1jOJy8=	2014-10-16 18:19:30.275692+02	f	grupoAB				f	t	2014-10-16 18:19:30.27575+02
1	pbkdf2_sha256$12000$wMTvaLW103hO$ZUYLP/jjp23Be8tspKDU6nIQfY1FiFPMPNlpD2rbzvk=	2014-10-17 10:50:44.243589+02	t	zeneke			zeneke@gmail.com	t	t	2014-09-18 12:46:26.487391+02
20	pbkdf2_sha256$12000$YkXInOGhB2NI$rkl+6QjQQsTko8crRQ87QGezinrGgubDvfL02s5JpZs=	2014-10-17 11:33:52.097366+02	f	ABCDgrupos				f	t	2014-10-17 11:33:52.097422+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_user_id_seq', 20, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2014-09-18 12:52:59.022206+02	2	fgimenez	1		4	1
2	2014-09-18 12:53:10.209112+02	1	Partido object	1		7	1
3	2014-09-18 12:53:18.983274+02	2	Partido object	1		7	1
4	2014-09-18 15:42:46.911076+02	1	Rank object	1		9	1
5	2014-09-18 15:42:55.967216+02	2	Rank object	1		9	1
6	2014-09-18 15:49:23.511279+02	3	agormaz	1		4	1
7	2014-09-18 15:49:48.962935+02	4	Partido object	1		7	1
8	2014-09-18 15:49:54.201989+02	5	Partido object	1		7	1
9	2014-09-18 15:50:13.585552+02	6	Partido object	1		7	1
10	2014-09-18 15:52:21.344248+02	3	Rank object	1		9	1
11	2014-09-18 16:08:24.41395+02	7	Partido object	1		7	1
12	2014-09-22 14:07:00.943743+02	8	asd	3		4	1
13	2014-09-22 14:07:01.132775+02	5	ferpis	3		4	1
14	2014-09-22 14:07:01.199004+02	4	ferpo	3		4	1
15	2014-09-22 14:07:01.20978+02	6	hola	3		4	1
16	2014-09-22 14:07:01.220953+02	7	oso	3		4	1
17	2014-09-22 14:07:01.23194+02	9	qwe	3		4	1
18	2014-09-22 14:25:31.467148+02	10	ferpo	3		4	1
19	2014-09-22 14:25:43.172277+02	11	da	3		4	1
20	2014-09-22 15:06:44.79632+02	1	Equipo object	1		8	1
21	2014-09-22 15:06:57.854201+02	2	Equipo object	1		8	1
22	2014-09-22 15:33:50.949059+02	1	Grupo object	1		10	1
23	2014-09-22 15:34:03.945706+02	2	Grupo object	1		10	1
24	2014-09-22 15:34:17.868889+02	3	Grupo object	1		10	1
25	2014-09-22 15:45:05.32859+02	3	Grupo object	3		10	1
26	2014-09-22 15:45:56.339255+02	3	Equipo object	1		8	1
27	2014-09-22 15:46:08.951304+02	4	Equipo object	1		8	1
28	2014-09-22 15:46:19.093339+02	5	Equipo object	1		8	1
29	2014-09-22 16:09:03.187809+02	5	España	2	Changed grupo.	8	1
30	2014-09-22 16:54:56.324189+02	14	nuevo	3		4	1
31	2014-09-22 16:54:56.364486+02	15	nuevo2	3		4	1
32	2014-09-22 16:54:56.375297+02	16	random	3		4	1
33	2014-10-16 11:50:11.043772+02	2	B	2	No fields changed.	10	1
34	2014-10-16 11:50:17.351702+02	4	C	1		10	1
35	2014-10-16 11:50:20.469014+02	5	D	1		10	1
36	2014-10-16 11:50:24.638765+02	6	F	1		10	1
37	2014-10-16 11:50:28.879745+02	7	G	1		10	1
38	2014-10-16 11:54:49.437421+02	6	F	2	Changed grupo_id.	10	1
39	2014-10-16 11:54:55.104385+02	7	G	2	Changed grupo_id.	10	1
40	2014-10-16 11:55:02.097269+02	8	E	1		10	1
41	2014-10-16 11:55:21.465568+02	9	H	1		10	1
42	2014-10-16 18:19:30.688576+02	19	grupoAB	1		4	1
43	2014-10-17 10:18:13.612668+02	6	Paises Bajos	1		8	1
44	2014-10-17 10:18:41.807527+02	7	Chile	1		8	1
45	2014-10-17 10:19:02.559061+02	8	Australia	1		8	1
46	2014-10-17 10:19:27.155469+02	9	Colombia	1		8	1
47	2014-10-17 10:19:45.687299+02	10	Grecia	1		8	1
48	2014-10-17 10:20:01.587318+02	11	Costa de Marfil	1		8	1
49	2014-10-17 10:20:15.186939+02	12	Japon	1		8	1
50	2014-10-17 11:08:35.20487+02	13	Uruguay	1		8	1
51	2014-10-17 11:08:50.374953+02	14	Costa Rica	1		8	1
52	2014-10-17 11:09:12.089779+02	15	Inglaterra	1		8	1
53	2014-10-17 11:09:25.339886+02	16	Italia	1		8	1
54	2014-10-17 11:09:41.986299+02	17	Suiza	1		8	1
55	2014-10-17 11:09:54.75686+02	18	Ecuador	1		8	1
56	2014-10-17 11:10:16.030526+02	19	Francia	1		8	1
57	2014-10-17 11:10:29.243745+02	20	Honduras	1		8	1
58	2014-10-17 11:21:03.142541+02	21	Argentina	1		8	1
59	2014-10-17 11:21:21.088696+02	22	Bosnia y Herzegovina	1		8	1
60	2014-10-17 11:21:32.215552+02	23	Iran	1		8	1
61	2014-10-17 11:21:46.836953+02	24	Nigeria	1		8	1
62	2014-10-17 11:22:04.35437+02	25	Alemania	1		8	1
63	2014-10-17 11:22:16.413483+02	26	Portugal	1		8	1
64	2014-10-17 11:22:30.17957+02	27	Ghana	1		8	1
65	2014-10-17 11:22:44.195041+02	28	EEUU	1		8	1
66	2014-10-17 11:22:57.949322+02	29	Belgica	1		8	1
67	2014-10-17 11:23:12.091173+02	30	Argelia	1		8	1
68	2014-10-17 11:23:21.9482+02	31	Rusia	1		8	1
69	2014-10-17 11:23:40.995358+02	32	Republica de Corea	1		8	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 69, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	partido	mundial2014	partido
8	equipo	mundial2014	equipo
9	rank	mundial2014	rank
10	grupo	mundial2014	grupo
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('django_content_type_id_seq', 10, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2014-09-18 11:55:39.123528+02
2	auth	0001_initial	2014-09-18 11:55:40.302995+02
3	admin	0001_initial	2014-09-18 11:55:40.58337+02
4	sessions	0001_initial	2014-09-18 11:55:40.78349+02
5	mundial2014	0001_initial	2014-09-18 12:38:15.632587+02
6	mundial2014	0002_rank	2014-09-18 15:41:49.877674+02
7	mundial2014	0003_auto_20140922_1406	2014-09-22 14:06:21.520716+02
8	mundial2014	0004_equipo_equipo_id	2014-09-22 15:06:02.365025+02
9	mundial2014	0005_grupo	2014-09-22 15:32:21.230975+02
10	mundial2014	0006_auto_20140922_1605	2014-09-22 16:05:23.09299+02
11	mundial2014	0007_auto_20140922_1634	2014-09-22 16:34:41.848142+02
12	mundial2014	0008_auto_20140922_1642	2014-09-22 16:43:01.366338+02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('django_migrations_id_seq', 12, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
scegmzu7tq9alyaf5eohr2ji63pe6a84	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-02 12:51:50.302507+02
ps08dykml0krmlefok0kdfna7hdd4o9u	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-07 11:51:59.157789+02
vsbi0rjdzvkw3o6ess8w4v3f7bge8ku0	ZGM5MzcxZmYxMDAzOWIyZGZjZmUyZDAxZjQ2OTAxNGZmYjJjYmMyNjp7fQ==	2014-10-29 10:41:59.542315+01
u8pdp4gtidnmwk8xqwn62eh3kp5xft2s	ZGM5MzcxZmYxMDAzOWIyZGZjZmUyZDAxZjQ2OTAxNGZmYjJjYmMyNjp7fQ==	2014-10-29 10:42:55.493477+01
0clhqjdjvfy3qjv0vcalavfg904dbtdo	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-29 18:10:50.389296+01
662bwyzz85fp3a4kqbuyjegp2t26pmv9	ZGM5MzcxZmYxMDAzOWIyZGZjZmUyZDAxZjQ2OTAxNGZmYjJjYmMyNjp7fQ==	2014-10-30 17:04:15.651711+01
o9lfji6gav70jengg4i1uejdys1o6hil	ODkyZDdlZTc4NzY2MmU2NzYwZjk5ZjJmNGI2M2U3ODlkMWZjMzZiNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImU2NDliN2EwNDE2YzU1MmY5NWFiMWUyNzU2ZDk5ZTZiMTk2YTQ0Y2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9	2014-10-30 17:57:32.82675+01
bkr3t006dxae8wp9rmgp48itmmrsaqsi	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-30 18:00:04.103589+01
sph0oxiyc1ua0w2u3b0rok0p4nqg9kic	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-30 18:19:11.394547+01
lidz7f0vcjohbo32gjc1uxcdqbcftdxr	MDNmOWRhODBkZjlhZWZhNmRmZGRmNjE4Y2ZiMjNjNTY3NGJiMTA2Nzp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc4MjVhY2ZlMzFhZmMyYzFlZmYxODgzZGJhMzRiMzQzNzlmMzllN2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2014-10-31 10:50:44.377159+01
\.


--
-- Data for Name: mundial2014_equipo; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY mundial2014_equipo (id, nombre, name, flag, equipo_id, grupo_id) FROM stdin;
1	Brasil	Brazil	br	1	1
2	Croacia	Croatia	cs	2	1
3	Mexico	Mexico	mx	3	1
4	Camerun	Camerun	cm	4	1
5	España	España	es	5	2
6	Paises Bajos	Paises Bajos	pa	6	2
7	Chile	Chile	cl	7	2
8	Australia	Australia	au	8	2
9	Colombia	Colombia	co	9	4
10	Grecia	Grecia	gr	10	4
11	Costa de Marfil	Costa de Marfil	cm	11	4
12	Japon	Japon	jp	12	4
13	Uruguay	Uruguay	uy	13	5
14	Costa Rica	Costa Rica	cr	14	5
15	Inglaterra	Inglaterra	england	15	5
16	Italia	Italia	it	16	5
17	Suiza	Suiza	sw	17	8
18	Ecuador	Ecuador	ec	18	8
19	Francia	Francia	fr	19	8
20	Honduras	Honduras	hn	20	8
21	Argentina	Argentina	ar	21	6
22	Bosnia y Herzegovina	Bosnia y Herzegovina	ba	22	6
23	Iran	Iran	ir	23	6
24	Nigeria	Nigeria	ng	24	6
25	Alemania	Alemania	alemania	25	7
26	Portugal	Portugal	pt	26	7
27	Ghana	Ghana	gh	27	7
28	EEUU	EEUU	us	28	7
29	Belgica	Belgica	be	29	9
30	Argelia	Argelia	argelia	30	9
31	Rusia	Rusia	ru	31	9
32	Republica de Corea	Republica de Corea	kr	32	9
\.


--
-- Name: mundial2014_equipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('mundial2014_equipo_id_seq', 32, true);


--
-- Data for Name: mundial2014_grupo; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY mundial2014_grupo (id, grupo_id, nombre) FROM stdin;
1	1	A
2	2	B
4	3	C
5	4	D
6	6	F
7	7	G
8	5	E
9	8	H
\.


--
-- Name: mundial2014_grupo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('mundial2014_grupo_id_seq', 9, true);


--
-- Data for Name: mundial2014_partido; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY mundial2014_partido (id, partido_id, usuario_id, local, local_id, visitante, visitante_id) FROM stdin;
1	1	2	0	0	0	0
3	3	2	0	0	0	0
4	1	3	0	0	0	0
5	2	3	0	0	0	0
6	3	3	0	0	0	0
7	1	1	0	0	0	0
8	1	13	0	0	0	0
9	2	13	0	0	0	0
10	3	13	0	0	0	0
12	5	13	0	0	0	0
13	6	13	0	0	0	0
14	7	13	0	0	0	0
15	8	13	0	0	0	0
16	9	13	0	0	0	0
17	10	13	0	0	0	0
18	11	13	0	0	0	0
19	12	13	0	0	0	0
20	13	13	0	0	0	0
21	14	13	0	0	0	0
22	15	13	0	0	0	0
23	16	13	0	0	0	0
24	17	13	0	0	0	0
25	18	13	0	0	0	0
26	19	13	0	0	0	0
27	20	13	0	0	0	0
28	21	13	0	0	0	0
29	22	13	0	0	0	0
30	23	13	0	0	0	0
31	24	13	0	0	0	0
32	25	13	0	0	0	0
33	26	13	0	0	0	0
34	27	13	0	0	0	0
35	28	13	0	0	0	0
36	29	13	0	0	0	0
37	30	13	0	0	0	0
38	31	13	0	0	0	0
39	32	13	0	0	0	0
40	33	13	0	0	0	0
41	34	13	0	0	0	0
42	35	13	0	0	0	0
43	36	13	0	0	0	0
44	37	13	0	0	0	0
45	38	13	0	0	0	0
46	39	13	0	0	0	0
47	40	13	0	0	0	0
48	41	13	0	0	0	0
49	42	13	0	0	0	0
50	43	13	0	0	0	0
51	44	13	0	0	0	0
52	45	13	0	0	0	0
53	46	13	0	0	0	0
54	47	13	0	0	0	0
55	48	13	0	0	0	0
56	49	13	0	0	0	0
57	50	13	0	0	0	0
58	51	13	0	0	0	0
59	52	13	0	0	0	0
60	53	13	0	0	0	0
61	54	13	0	0	0	0
62	55	13	0	0	0	0
63	56	13	0	0	0	0
64	57	13	0	0	0	0
65	58	13	0	0	0	0
66	59	13	0	0	0	0
67	60	13	0	0	0	0
68	61	13	0	0	0	0
69	62	13	0	0	0	0
70	63	13	0	0	0	0
200	2	17	4	1	0	27
201	3	17	2	1	3	7
202	4	17	1	15	2	28
203	5	17	2	23	4	30
204	6	17	2	4	3	7
205	7	17	1	15	0	26
206	8	17	3	8	2	30
207	9	17	2	5	3	17
208	10	17	1	21	3	3
209	11	17	4	23	2	14
211	13	17	2	23	2	14
212	14	17	2	28	1	13
213	15	17	4	25	0	27
214	16	17	2	25	3	12
215	17	17	3	18	2	8
216	18	17	2	21	0	19
217	19	17	2	24	0	11
218	20	17	1	22	4	2
219	21	17	2	7	2	14
220	22	17	4	15	0	13
221	23	17	2	20	3	9
222	24	17	3	24	3	11
223	25	17	4	2	0	15
224	26	17	2	18	3	21
225	27	17	3	13	0	20
226	28	17	1	16	0	18
227	29	17	2	14	1	6
228	30	17	0	8	0	19
229	31	17	3	9	3	24
230	32	17	1	9	3	27
231	33	17	4	5	4	10
232	34	17	2	27	4	18
233	35	17	1	22	1	27
234	36	17	2	29	4	1
235	37	17	2	17	4	24
236	38	17	0	15	2	13
237	39	17	0	25	3	3
238	40	17	4	28	4	27
239	41	17	2	13	4	8
240	42	17	2	10	4	3
241	43	17	0	14	0	23
242	44	17	0	1	3	7
243	45	17	3	27	1	16
244	46	17	4	10	0	26
245	47	17	1	21	4	14
246	48	17	0	27	1	8
247	49	17	1	13	0	14
248	50	17	0	11	0	9
2	2	2	0	0	3	0
199	1	17	2	15	4	12
249	51	17	0	1	3	1
250	52	17	2	24	3	13
251	53	17	0	13	2	18
252	54	17	3	31	3	22
253	55	17	1	25	4	31
254	56	17	0	7	1	23
255	57	17	0	22	4	17
256	58	17	0	30	3	31
257	59	17	2	9	4	18
258	60	17	1	4	1	3
259	61	17	4	3	1	2
260	62	17	2	8	4	2
261	63	17	2	9	2	13
262	64	17	3	1	3	23
11	4	13	5	0	5	0
210	12	17	2	21	4	26
263	1	18	4	30	2	29
264	2	18	0	25	0	6
265	3	18	3	6	0	19
266	4	18	0	15	3	21
267	5	18	4	1	4	27
268	6	18	0	30	1	31
269	7	18	1	4	2	7
270	8	18	0	6	3	9
271	9	18	2	12	2	8
272	10	18	1	7	4	30
273	11	18	3	31	4	25
274	12	18	4	8	2	2
275	13	18	4	21	2	25
276	14	18	3	14	1	11
277	15	18	4	10	0	22
278	16	18	1	2	3	19
279	17	18	4	25	3	9
280	18	18	2	20	2	29
281	19	18	4	11	2	8
282	20	18	0	8	4	17
283	21	18	1	27	1	12
284	22	18	3	15	3	3
285	23	18	4	14	0	7
286	24	18	1	14	3	3
287	25	18	2	4	0	16
288	26	18	2	7	0	21
289	27	18	0	26	0	20
290	28	18	2	8	1	17
291	29	18	3	31	3	2
292	30	18	2	16	1	11
293	31	18	4	4	0	1
294	32	18	0	18	0	29
295	33	18	2	17	2	10
296	34	18	4	10	0	30
297	35	18	1	22	4	30
298	36	18	0	18	1	2
299	37	18	2	17	3	6
300	38	18	2	15	2	1
301	39	18	2	11	0	7
302	40	18	2	19	1	27
303	41	18	0	5	4	22
304	42	18	0	12	4	27
305	43	18	3	10	4	30
306	44	18	3	4	2	14
307	45	18	1	11	4	8
308	46	18	0	19	0	15
309	47	18	0	5	2	17
310	48	18	1	20	3	25
311	49	18	2	21	4	30
312	50	18	2	17	2	24
313	51	18	2	9	4	15
314	52	18	3	29	1	21
315	53	18	2	6	3	22
316	54	18	1	31	3	10
317	55	18	3	30	2	29
318	56	18	3	17	2	14
319	57	18	3	9	1	7
320	58	18	2	11	0	4
321	59	18	4	21	0	22
322	60	18	4	23	0	13
323	61	18	2	5	4	29
324	62	18	1	25	0	12
325	63	18	1	7	3	24
326	64	18	2	2	0	26
327	1	19	2	1	1	2
328	2	19	2	3	3	4
329	17	19	2	1	1	3
330	18	19	0	4	1	2
331	33	19	0	4	4	1
332	34	19	2	2	1	3
333	3	19	0	5	2	6
334	4	19	3	7	1	8
335	20	19	0	5	1	7
336	19	19	2	8	1	6
337	35	19	1	8	4	5
338	36	19	3	6	4	7
339	1	20	2	1	1	2
340	2	20	3	3	2	4
341	17	20	0	1	1	3
342	18	20	3	4	2	2
343	33	20	3	4	1	1
344	34	20	0	2	3	3
345	3	20	2	5	0	6
346	4	20	1	7	3	8
347	19	20	0	5	3	7
348	20	20	0	8	2	6
349	35	20	3	8	0	5
350	36	20	3	6	1	7
351	5	20	0	9	0	10
352	6	20	1	11	3	12
353	21	20	2	9	2	11
354	22	20	2	12	0	10
355	37	20	3	12	3	9
356	38	20	3	10	3	11
357	7	20	3	13	0	14
358	8	20	0	15	3	16
359	23	20	2	13	1	15
360	24	20	1	16	1	14
361	39	20	3	16	1	13
362	40	20	3	14	2	15
\.


--
-- Name: mundial2014_partido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('mundial2014_partido_id_seq', 362, true);


--
-- Data for Name: mundial2014_rank; Type: TABLE DATA; Schema: public; Owner: zeneke
--

COPY mundial2014_rank (id, puntos, usuario_id) FROM stdin;
1	5	2
2	3	1
3	23	3
5	0	12
6	0	13
10	0	17
11	0	18
12	0	19
13	0	20
\.


--
-- Name: mundial2014_rank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zeneke
--

SELECT pg_catalog.setval('mundial2014_rank_id_seq', 13, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: mundial2014_equipo_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY mundial2014_equipo
    ADD CONSTRAINT mundial2014_equipo_pkey PRIMARY KEY (id);


--
-- Name: mundial2014_grupo_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY mundial2014_grupo
    ADD CONSTRAINT mundial2014_grupo_pkey PRIMARY KEY (id);


--
-- Name: mundial2014_partido_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY mundial2014_partido
    ADD CONSTRAINT mundial2014_partido_pkey PRIMARY KEY (id);


--
-- Name: mundial2014_rank_pkey; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY mundial2014_rank
    ADD CONSTRAINT mundial2014_rank_pkey PRIMARY KEY (id);


--
-- Name: mundial2014_rank_usuario_id_527626b9871b784d_uniq; Type: CONSTRAINT; Schema: public; Owner: zeneke; Tablespace: 
--

ALTER TABLE ONLY mundial2014_rank
    ADD CONSTRAINT mundial2014_rank_usuario_id_527626b9871b784d_uniq UNIQUE (usuario_id);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: mundial2014_equipo_acaeb2d6; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX mundial2014_equipo_acaeb2d6 ON mundial2014_equipo USING btree (grupo_id);


--
-- Name: mundial2014_partido_abfe0f96; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX mundial2014_partido_abfe0f96 ON mundial2014_partido USING btree (usuario_id);


--
-- Name: mundial2014_rank_abfe0f96; Type: INDEX; Schema: public; Owner: zeneke; Tablespace: 
--

CREATE INDEX mundial2014_rank_abfe0f96 ON mundial2014_rank USING btree (usuario_id);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mundial2014_eq_grupo_id_cab5694febac19b_fk_mundial2014_grupo_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_equipo
    ADD CONSTRAINT mundial2014_eq_grupo_id_cab5694febac19b_fk_mundial2014_grupo_id FOREIGN KEY (grupo_id) REFERENCES mundial2014_grupo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mundial2014_partido_usuario_id_24a98506593cf175_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_partido
    ADD CONSTRAINT mundial2014_partido_usuario_id_24a98506593cf175_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mundial2014_rank_usuario_id_527626b9871b784d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: zeneke
--

ALTER TABLE ONLY mundial2014_rank
    ADD CONSTRAINT mundial2014_rank_usuario_id_527626b9871b784d_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


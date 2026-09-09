-- Active: 1788283833530@@127.0.0.1@5432@pizzaria
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

CREATE TABLE cardapio (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

CREATE TYPE status_ped_enum AS ENUM (
    'Pendente',
    'Pronto', 
    'Entregue'
); 
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    total DECIMAL(10, 2) CHECK (total > 0),
    status status_ped_enum DEFAULT 'Pendente',
    data TIMESTAMP DEFAULT now(),
    cliente_id INT REFERENCES clientes(id)
);

CREATE TABLE itens_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INT REFERENCES pedidos(id),
    cardapio_id INT REFERENCES cardapio(id),
    quantidade INT CHECK (quantidade > 0)
);
import React, { useState, useEffect } from "react";

function GastosApp() {
  const [categoria, setCategoria] = useState("");
  const [valor, setValor] = useState("");
  const [itens, setItens] = useState([]);
  const [mensagem, setMensagem] = useState("");

  // Carrega itens ao iniciar
  useEffect(() => {
    listarItens();
  }, []);

  async function adicionarItem(e) {
    e.preventDefault();
    if (!categoria || !valor) {
      setMensagem("Preencha todos os campos.");
      return;
    }
    const response = await fetch("/adicionar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ categoria, valor }),
    });
    const result = await response.json();
    setMensagem(result.message);
    setCategoria("");
    setValor("");
    listarItens();
  }

  async function listarItens() {
    const response = await fetch("/listar");
    const data = await response.json();
    setItens(data.itens);
  }

  return (
    <div style={{ maxWidth: 400, margin: "auto" }}>
      <h1>Listagem de Gastos</h1>
      <form onSubmit={adicionarItem}>
        <input
          placeholder="Categoria"
          value={categoria}
          onChange={e => setCategoria(e.target.value)}
        />
        <input
          placeholder="Valor"
          type="number"
          step="0.01"
          value={valor}
          onChange={e => setValor(e.target.value)}
        />
        <button type="submit">Adicionar</button>
      </form>
      {mensagem && <p>{mensagem}</p>}
      <h2>Itens</h2>
      <ul>
        {itens.map((item, idx) => (
          <li key={idx}>
            {item.categoria}: {item.valor}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GastosApp;
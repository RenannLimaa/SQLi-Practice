function updateQuery() {
  const input = document.getElementById("employee_id").value;
  const idPart = input.split(" ")[0];  // Simula explode(' ', x)[0]
  const query = `SELECT name FROM employees WHERE id = CAST(${idPart} AS INT)`;
  document.getElementById("query-output").innerText = query;
}

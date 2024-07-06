const express = require('express');
const app = express();
app.use(express.json());

app.post('/detectar_idiomas', (req, res) => {
  const { textos } = req.body;
  if (textos) {
    const idiomasDetectados = textos.map(texto => texto.includes('es') ? 'español' : 'inglés');
    return res.json({ idiomas_detectados: idiomasDetectados });
  }
  return res.status(400).json({ error: 'No se proporcionaron textos' });
});

app.post('/extraer_argumentos', (req, res) => {
  const { textos } = req.body;
  if (textos) {
    const argumentos = textos.map(texto => ({ texto, argumento: 'simulado' }));
    return res.json({ argumentos });
  }
  return res.status(400).json({ error: 'No se proporcionaron textos' });
});

app.listen(3000, () => {
  console.log('Servidor corriendo en el puerto 3000');
});

module.exports = app;

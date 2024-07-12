const express = require('express');
const app = express();
app.use(express.json());

const handlePostRequest = (req, res, callback) => {
  const { textos } = req.body;
  if (textos) {
    const result = callback(textos);
    return res.json(result);
  }
  return res.status(400).json({ error: 'No se proporcionaron textos' });
};

app.post('/detectar_idiomas', (req, res) => {
  handlePostRequest(req, res, textos => ({
    idiomas_detectados: textos.map(texto => texto.includes('es') ? 'español' : 'inglés')
  }));
});

app.post('/extraer_argumentos', (req, res) => {
  handlePostRequest(req, res, textos => ({
    argumentos: textos.map(texto => ({ texto, argumento: 'simulado' }))
  }));
});

app.listen(3000, () => {
  console.log('Servidor corriendo en el puerto 3000');
});

module.exports = app;

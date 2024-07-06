const request = require('supertest');
const app = require('../src/main'); // Ajusta la ruta según la ubicación de tu archivo main.js

describe('POST /detectar_idiomas', () => {
  it('debería detectar idiomas correctamente', async () => {
    const res = await request(app)
      .post('/detectar_idiomas')
      .send({ textos: ['es un texto', 'this is a text'] });
    expect(res.statusCode).toEqual(200);
    expect(res.body.idiomas_detectados).toEqual(['español', 'inglés']);
  });

  it('debería devolver un error si no se proporcionan textos', async () => {
    const res = await request(app).post('/detectar_idiomas').send({});
    expect(res.statusCode).toEqual(400);
    expect(res.body.error).toBe('No se proporcionaron textos');
  });
});

describe('POST /extraer_argumentos', () => {
  it('debería extraer argumentos correctamente', async () => {
    const res = await request(app)
      .post('/extraer_argumentos')
      .send({ textos: ['es un texto', 'this is a text'] });
    expect(res.statusCode).toEqual(200);
    expect(res.body.argumentos).toEqual([
      { texto: 'es un texto', argumento: 'simulado' },
      { texto: 'this is a text', argumento: 'simulado' }
    ]);
  });

  it('debería devolver un error si no se proporcionan textos', async () => {
    const res = await request(app).post('/extraer_argumentos').send({});
    expect(res.statusCode).toEqual(400);
    expect(res.body.error).toBe('No se proporcionaron textos');
  });
});

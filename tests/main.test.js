const request = require('supertest');
const app = require('../src/main');

// Función de ayuda para realizar solicitudes POST
const postRequest = async (endpoint, body) => {
  return await request(app).post(endpoint).send(body);
};

describe('POST /detectar_idiomas', () => {
  it('debería detectar idiomas correctamente', async () => {
    const res = await postRequest('/detectar_idiomas', { textos: ['es un texto', 'this is a text'] });
    expect(res.statusCode).toEqual(200);
    expect(res.body.idiomas_detectados).toEqual(['español', 'inglés']);
  });

  it('debería devolver un error si no se proporcionan textos', async () => {
    const res = await postRequest('/detectar_idiomas', {});
    expect(res.statusCode).toEqual(400);
    expect(res.body.error).toBe('No se proporcionaron textos');
  });
});

describe('POST /extraer_argumentos', () => {
  it('debería extraer argumentos correctamente', async () => {
    const res = await postRequest('/extraer_argumentos', { textos: ['es un texto', 'this is a text'] });
    expect(res.statusCode).toEqual(200);
    expect(res.body.argumentos).toEqual([
      { texto: 'es un texto', argumento: 'simulado' },
      { texto: 'this is a text', argumento: 'simulado' }
    ]);
  });

  it('debería devolver un error si no se proporcionan textos', async () => {
    const res = await postRequest('/extraer_argumentos', {});
    expect(res.statusCode).toEqual(400);
    expect(res.body.error).toBe('No se proporcionaron textos');
  });
});


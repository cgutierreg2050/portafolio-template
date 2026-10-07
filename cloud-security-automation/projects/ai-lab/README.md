# 16. Infraestructura local para IA – RTX 3060, 128 GB RAM y Ryzen 9

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Laboratorio implementado para pruebas.

Laboratorio Ubuntu con Ryzen 9, 128 GB RAM y RTX 3060 de 12 GB; CUDA, Python, PyTorch y modelos cuantizados.

**Tecnologías del caso:** Ubuntu · CUDA · PyTorch · Python · Hugging Face.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `11551551`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Estima el tamaño mínimo de pesos según parámetros y precisión, con una reserva configurable.

```text
Model parameters → precision → weight estimate → available memory comparison
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py ai-lab
python3 demo.py ai-lab --output generated/ai-lab.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `ai_lab`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No garantiza que un modelo funcione en GPU: excluye KV cache, activaciones, metadatos y sobrecarga del runtime.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Local AI infrastructure and prototyping lab** — Lab implemented for testing.

Ubuntu lab with Ryzen 9, 128 GB RAM and a 12 GB RTX 3060; CUDA, Python, PyTorch and quantized models.

**Demonstration:** Estimates a lower bound for weight memory from parameter count and precision, with configurable reserve.

**Boundary:** Does not guarantee GPU inference fit: excludes KV cache, activations, metadata and runtime overhead.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

# 18. LexRAG Analytics | IA privada para consulta y análisis documental

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Indexación y validación.

Plataforma con OCR, embeddings, Qdrant, FastAPI, Ollama y Docker. Recuperación y respuestas en validación; análisis estadístico como fase futura.

**Tecnologías del caso:** Python · FastAPI · Qdrant · Ollama · Docker · OCR · RAG.

[Fuente pública](https://www.linkedin.com/feed/update/urn:li:activity:7489795833895342080/) · Proyecto de LinkedIn `256024915`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Busca términos en documentos ficticios autorizados y devuelve referencias a la fuente, o indica falta de evidencia.

```text
Query → access filter → lexical scoring → source citations
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py lexrag
python3 demo.py lexrag --output generated/lexrag.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `document_retrieval`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** Es una línea base léxica, no búsqueda semántica, OCR, embeddings ni generación de respuestas.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**LexRAG private document retrieval** — Indexing and validation.

OCR, embeddings, Qdrant, FastAPI, Ollama and Docker platform. Retrieval and responses under validation; statistical analysis is a future phase.

**Demonstration:** Searches authorized synthetic documents for terms and returns source references, or no evidence.

**Boundary:** Lexical baseline only, not semantic retrieval, OCR, embeddings or generated answers.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

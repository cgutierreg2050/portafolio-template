# 06. Automatización de comunicaciones con Python y Microsoft Graph

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Aplicación documentada para más de 8.000 correos diarios con HTML, adjuntos, campos personalizados y procesamiento por lotes.

**Tecnologías del caso:** Python · Microsoft Graph · Microsoft 365.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `433570211`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Construye borradores HTML escapados, elimina destinatarios repetidos y organiza lotes con claves de seguimiento.

```text
Recipients → validation → deduplication → draft batches
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py graph-mail
python3 demo.py graph-mail --output generated/graph-mail.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `graph_messages`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No envía mensajes, adjunta archivos ni implementa reintentos de Graph. Las claves locales no garantizan idempotencia del servicio.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Python and Microsoft Graph communications** — Implemented, as described in the published case.

Documented application supporting 8,000+ daily messages with HTML, attachments, personalization and batch processing.

**Demonstration:** Builds escaped HTML drafts, deduplicates recipients and groups batches with tracking keys.

**Boundary:** No messages, attachments or Graph retries. Local tracking keys do not provide service-level idempotency.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

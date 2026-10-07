# 03. Automatización de transcripción masiva con IA y control de GPU

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Transcripción por lotes con Python, Whisper, CUDA y control de VRAM; organización de archivos y manejo de errores.

**Tecnologías del caso:** Python · Whisper · CUDA · pynvml · Linux.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `716038611`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Organiza trabajos ficticios en lotes que respetan un presupuesto de memoria y separa trabajos demasiado grandes.

```text
Audio metadata → VRAM budget → batches → rejected jobs
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py transcription
python3 demo.py transcription --output generated/transcription.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `transcription`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No carga Whisper, utiliza la GPU ni procesa audio. Las estimaciones de memoria son entradas del ejemplo, no mediciones.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Batch transcription and GPU resource control** — Implemented, as described in the published case.

Batch transcription with Python, Whisper, CUDA, VRAM controls, file organization and error handling.

**Demonstration:** Packs synthetic jobs into batches within a declared memory budget and separates oversized jobs.

**Boundary:** Does not load Whisper, use a GPU or process audio. Memory estimates are fixture inputs, not measurements.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

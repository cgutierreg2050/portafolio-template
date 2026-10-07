# 07. Automatización de consultas con Docker y Selenium | 13 workers

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Automatización en Linux con Selenium y Docker, escalada de uno a trece contenedores independientes.

**Tecnologías del caso:** Python · Docker · Selenium · Linux.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `171967654`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Distribuye trabajos ficticios por costo estimado entre varios workers. También se conserva el ejemplo Docker/Selenium sobre una página local.

```text
Jobs → estimated cost → worker assignment → simulated load
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py docker-selenium
python3 demo.py docker-selenium --output generated/docker-selenium.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `container_queue`](../../lab/operations.py) · [Pruebas](../../tests/test_catalog.py)

Ejemplo Docker/Selenium: [instrucciones](../../docs/runbook.md).

**Límite del ejemplo:** El planificador simula la asignación; no inicia contenedores ni demuestra rendimiento. El ejemplo Docker tiene su propia validación separada.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Docker and Selenium query automation** — Implemented, as described in the published case.

Linux Selenium automation scaled from one to thirteen independent Docker containers.

**Demonstration:** Allocates synthetic jobs across workers by estimated cost. The existing Docker/Selenium local-page example is retained.

**Boundary:** The scheduler simulates allocation; it starts no containers and is not a performance benchmark. Docker has separate validation.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

# 11. Despliegue de n8n en Kubernetes + Cloudflare Tunnel

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Despliegue de n8n, acceso con Cloudflare Zero Trust e integración con CI/CD para automatizaciones internas.

**Tecnologías del caso:** n8n · Kubernetes · Cloudflare Tunnel · Zero Trust · CI/CD.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `428229201`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Revisa persistencia, readiness, referencia de clave de cifrado, servicio interno, túnel y política de acceso.

```text
Deployment inventory → configuration checks → review report
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py n8n-kubernetes
python3 demo.py n8n-kubernetes --output generated/n8n-kubernetes.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `n8n_config`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** Es un inventario simplificado, no un manifiesto desplegable. No demuestra alta disponibilidad.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**n8n on Kubernetes with Cloudflare Tunnel** — Implemented, as described in the published case.

n8n deployment with Cloudflare Zero Trust access and CI/CD integration for internal workflows.

**Demonstration:** Reviews persistence, readiness, encryption-key reference, internal service, tunnel and access policy.

**Boundary:** A simplified inventory, not a deployable manifest. High availability is not validated.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

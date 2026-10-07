# 05. Automatización con Terraform + GitHub Actions

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Aprovisionamiento de recursos Azure con Terraform y validaciones de cambios mediante GitHub Actions.

**Tecnologías del caso:** Terraform · GitHub Actions · Azure · IaC.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `433360439`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Revisa un plan simplificado para identificar reemplazos, eliminaciones, exposición administrativa y etiquetas faltantes.

```text
Proposed resources → policy checks → findings → manual review
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py terraform
python3 demo.py terraform --output generated/terraform.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `terraform_review`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** El formato JSON es didáctico y no es un export compatible de Terraform. No ejecuta terraform plan/apply ni despliega recursos.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Terraform and GitHub Actions automation** — Implemented, as described in the published case.

Azure resource provisioning with Terraform and change validation through GitHub Actions.

**Demonstration:** Reviews a simplified plan for replacements, deletions, management exposure and missing tags.

**Boundary:** The JSON schema is illustrative, not a Terraform plan export. Does not run Terraform or deploy resources.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

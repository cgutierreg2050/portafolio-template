# 09. Control de aplicaciones con AppLocker y WDAC

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Políticas de control de aplicaciones, excepciones controladas y validación de endpoints mediante GPO, PowerShell y Defender.

**Tecnologías del caso:** AppLocker · WDAC · GPO · PowerShell · Defender.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `348365288`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Evalúa reglas ficticias por hash o editor, con prioridad de denegación y distinción entre auditoría y aplicación.

```text
Application metadata → matching rules → deny precedence → decision
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py applocker-wdac
python3 demo.py applocker-wdac --output generated/applocker-wdac.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `app_control`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No genera una política Windows ni sustituye el motor de AppLocker/WDAC. Hashes y editores son inventados.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Application control with AppLocker and WDAC** — Implemented, as described in the published case.

Application-control policies, controlled exceptions and endpoint validation through GPO, PowerShell and Defender.

**Demonstration:** Evaluates synthetic hash/publisher rules with deny precedence and audit-versus-enforcement outcomes.

**Boundary:** Not a Windows policy generator or an AppLocker/WDAC engine. Hashes and publishers are invented.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

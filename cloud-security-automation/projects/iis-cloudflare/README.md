# 23. Publicación de sitios IIS con Cloudflare WAF + SSL

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

Publicación de dos portales IIS con certificado SSL, Cloudflare WAF, reglas Zero Trust y túneles cifrados.

**Tecnologías del caso:** IIS · Cloudflare WAF · TLS · Zero Trust · Tunnels.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `428753795`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Revisa metadatos ficticios de TLS al origen, WAF, política de acceso, exposición directa y caducidad de certificado.

```text
Portal configuration snapshot → exposure/TLS checks → review
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py iis-cloudflare
python3 demo.py iis-cloudflare --output generated/iis-cloudflare.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `iis_exposure`](../../lab/security.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** No se conecta a IIS o Cloudflare ni inspecciona certificados reales. La lista de controles es ilustrativa y parcial.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**IIS publishing with Cloudflare WAF and TLS** — Implemented, as described in the published case.

Publication of two IIS portals with SSL, Cloudflare WAF, Zero Trust access rules and encrypted tunnels.

**Demonstration:** Reviews synthetic origin TLS, WAF, access policy, direct exposure and certificate expiry metadata.

**Boundary:** No IIS/Cloudflare connections or real certificate inspection. The checklist is illustrative and incomplete.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

# 10. Despliegue de VM en Azure + VPN Site-to-Site

[Índice ES](../../README.es.md) · [Index EN](../../README.md)

## Caso profesional

**Estado:** Implementado, según el caso publicado.

VM Azure como controlador de dominio adicional y conectividad híbrida con VPN Site-to-Site y Fortinet.

**Tecnologías del caso:** Azure VM · Fortinet · VPN · Active Directory · DNS.

[Fuente pública](https://www.linkedin.com/in/kristiangutierrez/details/projects/) · Proyecto de LinkedIn `428864932`. El título de esta ficha permite localizar el caso en el perfil.

## Demostración con datos ficticios

Valida solapamiento de redes, pertenencia de la VM, rutas declaradas y reenvío DNS.

```text
Network plan → overlap checks → route checks → findings
```

```sh
# Desde cloud-security-automation; Python 3.11+, biblioteca estándar.
python3 demo.py azure-vpn
python3 demo.py azure-vpn --output generated/azure-vpn.json
```

[Datos de entrada](input.json) · [Salida de muestra](output.example.json) · [Implementación: `vpn_topology`](../../lab/cloud.py) · [Pruebas](../../tests/test_catalog.py)

**Límite del ejemplo:** Usa redes reservadas para documentación. No crea una VPN ni verifica paquetes, cifrado o replicación.

Los datos se crearon desde cero para este portafolio. El código es una reconstrucción demostrativa preparada con asistencia de IA a partir de la descripción del caso. Los resultados sintéticos no acreditan métricas de producción ni amplían el estado del proyecto profesional.

## English

**Azure VM and site-to-site VPN** — Implemented, as described in the published case.

Azure VM as an additional domain controller, with Fortinet site-to-site hybrid connectivity.

**Demonstration:** Checks network overlap, VM address membership, declared routes and DNS forwarding.

**Boundary:** Uses documentation networks. Does not create a VPN or validate packets, encryption or replication.

Run the commands above from the package directory. The fixture and output are synthetic; the code is an AI-assisted illustrative reconstruction, not production evidence. See the [data policy](../../docs/data-policy.md).

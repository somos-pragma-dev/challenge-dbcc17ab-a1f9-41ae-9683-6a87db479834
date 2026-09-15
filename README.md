# Fundamentos de API REST con Django Rest Framework y Autenticación

La empresa necesita desarrollar una API REST que permita a los clientes autenticarse y realizar consultas sobre sus transacciones financieras. La API debe manejar la autenticación de usuarios y proporcionar endpoints para consultar el historial de transacciones. El sistema debe asegurar que solo usuarios autenticados puedan acceder a sus datos y que la información se maneje de manera segura.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | python-django-rest |
| **Nivel** | junior-l1 |
| **Tipo** | theoretical |
| **Tiempo estimado** | 2 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración del Dominio

**Objetivo:** Comprender las necesidades del negocio y los requerimientos funcionales de la API REST.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Identifica los actores involucrados en el proceso (usuarios, sistema de autenticación, sistema de transacciones).
- Enumera las operaciones que la API debe soportar (autenticación, consulta de transacciones).
- Define los criterios de aceptación para cada operación (usuarios autenticados, datos correctos, seguridad de la información).

**Entregable:** Documento que describe los actores, operaciones y criterios de aceptación.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las implicaciones de seguridad en cada operación.
- Piensa en los posibles escenarios de uso y cómo la API los soporta.

</details>

### Fase 2: Diseño de la API

**Objetivo:** Diseñar la estructura de la API REST, incluyendo endpoints y métodos HTTP.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Define los endpoints necesarios para la autenticación y consulta de transacciones.
- Especifica los métodos HTTP apropiados para cada endpoint (GET, POST, etc.).
- Determina los parámetros de entrada y salida para cada endpoint.

**Entregable:** Diagrama de la estructura de la API, incluyendo endpoints y métodos HTTP.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la conveniencia de usar JSON Web Tokens (JWT) para la autenticación.
- Piensa en cómo manejar errores y excepciones en los endpoints.

</details>

### Fase 3: Consideraciones de Seguridad

**Objetivo:** Identificar y mitigar riesgos de seguridad en la API REST.

**Tiempo estimado:** 40 minutos

**Instrucciones:**

- Enumera los posibles riesgos de seguridad en la API (inyección SQL, ataques de fuerza bruta, etc.).
- Propone medidas para mitigar cada riesgo identificado.
- Discute las implicaciones de usar JWT para la autenticación.

**Entregable:** Documento que describe los riesgos de seguridad identificados y las medidas de mitigación propuestas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de HTTPS para asegurar la comunicación.
- Piensa en la implementación de límites de intentos de autenticación para prevenir ataques de fuerza bruta.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuáles son sus componentes principales?
- **paraQueSirve**: ¿Para qué sirve la autenticación en una API REST y cómo se implementa?
- **comoSeUsa**: ¿Cómo se usan los endpoints en una API REST para consultar transacciones?
- **erroresComunes**: ¿Cuáles son los errores comunes en la implementación de una API REST y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica el uso de JWT para la autenticación en una API REST?

## Criterios de Evaluacion

- Identificación correcta de los actores y operaciones en el dominio.
- Diseño adecuado de la estructura de la API con endpoints y métodos HTTP.
- Propuesta de medidas efectivas para mitigar riesgos de seguridad.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
el comando de build o arranque canonico del stack elegido
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*

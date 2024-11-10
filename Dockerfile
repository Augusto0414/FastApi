FROM python:3.13.0-alpine as builder

RUN apk add --no-cache \
    curl \
    bash \
    ca-certificates \
    && apk add --no-cache nodejs npm \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN rm -f /usr/local/bin/prisma

RUN npm install -g prisma@5.11.0

RUN npx prisma generate

# Etapa 2: Construcción de la imagen final
FROM python:3.13.0-alpine

RUN apk add --no-cache libpq

WORKDIR /app
COPY --from=builder /app /app

ENV DATABASE_URL=${DATABASE_URL}

CMD ["sh", "-c", "npx prisma migrate dev && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

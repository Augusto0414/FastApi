FROM python:3.13.0-alpine as builder

RUN apk add --no-cache \
    curl \
    bash \
    ca-certificates \
    gcc \
    musl-dev \
    python3-dev \
    && apk add --no-cache nodejs npm \
    && rm -rf /var/cache/apk/*

WORKDIR /app

COPY . .

# Install Python requirements including prisma client
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir prisma uvicorn

RUN rm -f /usr/local/bin/prisma

RUN npm install -g prisma@5.11.0

# Generate Prisma client
RUN prisma generate

# Final stage
FROM python:3.13.0-alpine

# Install required packages including nodejs and npm in the final image
RUN apk add --no-cache \
    libpq \
    nodejs \
    npm \
    gcc \
    musl-dev \
    python3-dev

WORKDIR /app
COPY --from=builder /app /app

# Install Python dependencies in the final image
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir prisma uvicorn

ENV DATABASE_URL=${DATABASE_URL}

# Modified command to use prisma instead of npx prisma
CMD ["sh", "-c", "prisma migrate dev && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
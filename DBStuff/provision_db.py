from sqlalchemy import create_engine
import Schema, engine
engine = engine.engine

Schema.mapper_registry.metadata.create_all(engine)

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


notice_releases = Table(
    "notice_releases",
    Base.metadata,
    Column("notice_id", Integer, ForeignKey("notice.id")),
    Column("release_id", String, ForeignKey("release.id")),
)


class Package(Base):
    __tablename__ = "package"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Release(Base):
    __tablename__ = "release"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Notice(Base):
    __tablename__ = "notice"

    id = Column(String, primary_key=True)
    title = Column(String)
    published = Column(DateTime)
    summary = Column(String)
    details = Column(String)
    instructions = Column(String)
    packages = Column(String)
    releases = relationship("Release", secondary=notice_releases)

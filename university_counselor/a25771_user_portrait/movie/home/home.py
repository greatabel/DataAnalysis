from flask import Flask, request
from flask import Blueprint, render_template


# from movie.adapters.memory_repository import load_movies
import movie.adapters.repository as repo
# from movie.domain.model import Director, User, Review, Movie
from movie.domain.model import Director, Review, Movie



# Brea's Capstone Proposal

## Name: Aoede

## Project Overview
Preferred music is one of the quickest ways to establish rapport and trust with a music therapy client. Analyzing a meaningful song from a client's favorite singer or playing and upbeat Broadway tune to entrain their gait can help a client stay motivated and find success in therapy. However, music therapists are often faced with a tsunami of potential music to be familiar with. As an educator and clinician, I often find myself lost when trying to prepare for a session when a client requests music from an artist or genre I'm not personally familiar with. Do I search the top hits on Spotify and miss a potentially obscure song with the perfect lyrical content? Or, do I quickly listen through for a high energy song, but miss the lyric content that sends a negative message? 

The Aoede (named after the muse of music) web application will provide an open access resource for music therapists to make and find clinical repertoire recommendations. Board-certified music therapists or other interested users will be able to use their own personal music expertise to make song repertoire suggestions for the community. Users may make these recommendations that weigh several musical and non-musical elements. For example, if a user is very familiar with Ingrid Michaelson's catalog, they may list the top five of Michaelson's songs that balance general popularity, therapeutic themes within the lyrics, and the playability of the chord progression. Over hundreds of these recommendations, the app will rank song recommendations across multiple users inputs for the purpose of helping music therapists target improve their clinical reperotire efficiently. With enough community input, other users can search by artist, genre, musical features, or thematic tags. Ideally, these songs would be able to be heard within the app and added to a user's personal Spotify playlist for listening and practicing.

## Functionality
Users of the Aoede app may fulfill one of two main functions: 1) Contributor or 2) Explorer.

In the Contributor role, users will be able to choose a primary element (musical or non-musical) by which to make song recommendations. These primary elements may be by artist (e.g., Beyonce), genre (e.g., Jazz), a musical element (e.g., fast tempo, lyric theme about resilience) or other non-musical tags of interest (e.g., Best songs for a beginning music therapy student). Users will then submit a song that they feel best exemplifies that primary element, or is prototypical of that element on a Likert Scale from 1-7. Users will have the choice to also rank the song from 1-7 on several pre-determined elements (e.g., fast-slow tempo, positivity of lyrics, what genre the song exemplifies, etc.). Users will be able to also submit a Spotify link or Wikipedia to the song and/or artist that they just submitted.

In the Explorer role, users will be able to search for songs based on a musical or non-musical element and see Contributors' rankings for that element, along with the average score of how that song exemplifies that element from 1-7. Rankings will be aggregated across all contributors' inputs. Explorers may then click a song to see the song's meta information as input by contributors. For example, if "We Will Rock You" is listed as the top percussive song, the song's individual profile would have a Spotify link so that the Explorer could hear the song, find a link to the Queen page on Wikipedia, and see other numeric scores for secondary elements or tags as rated by Contributors (e.g., 5.5 for fast tempo, popularity).


## Data Model
My Database will initially organize data from three classes:

Song Info
    - ID
    - Song Title
    - Artist
    - Release Year
    - Spotify Link
    - Wikipedia Link
    - (Links to other tables, Foreign Keys)

Music Tags
    - ID
    -Song Title
    - Genre
        - Likert rating on how the song represents x genre
    - Tempo
    - Singability
    - Playability of Harmonic Progression
    - Musical Mode
    - Dynamic Variability
    - Prominent Instruments
    - Use of Repetition
    - Balance of Vocal vs. Instrumental

Non-Music Tags
    - ID
    - Song Title
    - Arousal (high vs. low)
    - Emotional Ratings (1-7 for how they express the following emotions)
        - Happy
        - Sad
        - Angry
        - Fearful
        - Peaceful 
        - Brave
        - Challenging
        - Nostalgic
    - Culture (?)
    - Lyrical Theme Tags
    
## Schedule
Week 1 (June 29th):
- Build a functional database
- Build a basic Contributor input form 
    - Likert slider
    - Text Input
    - Spotify and Wikipedia links
    - Secondary Tags for Songs

- Set up basic html structure for a song's individual profile page

Week 2 (July 6th):
- Initial Html/CSS look of the website
- Figure out ranking and display system for elements/tags
- Build initial landing page

Week 3 (July 13th):
- Figure out search bar
- Allow contributors to make a new page for a new artist/tag
- Refine Html/CSS look of the website

Stretch Goals (July 20th):
- Individual user profiles
- Way to display Contributors' "rankings" based on how many recommendations they've contributed
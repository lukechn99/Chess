# Chess
### 3.1 Tactics, Board Evaluation, and Specifics

The first component of a chess-playing artificial intelligence program is the board evaluator. The
evaluator is used to determine the state of the board; typically, a board state is evaluated on the scale
of negative to positive numbers with a larger absolute negative number signifying the board as being
in favor of black and a larger positive number signifying the board as being in favor of white. Each
move that a player makes will affect the board score; white capturing a black pawn will result in the
score moving by +1. However, chess board evaluation often goes much deeper than directly adding
or subtracting a capture from the board score. Take, for example, a sacrifice, where white sacrifices a
pawn in order to move in position to capture a rook. Although the score should change by -1 for the
pawn capture, the future threat of a rook capture has a non-negligible impact on the score. Looking
at purely material is considered the most simplistic approach.[Gil03] Exploration into how we can go
deeper in evaluating a chess board requires a more developed knowledge domain representation. Some
of the proposed components of this representation include situations to be recognized, problems to be
stated, results to be expressed, and intermediate knowledge to be saved.[Ber74]

When it comes to tactics and board evaluation, it is extremely important to have a specific strategy
outline to follow so that a given algorithm can be coded and implemented. One recommended approach
is to first having the chess AI look for checkmate opportunities, then play ”good moves” (that likely
contributes to a favorable ratio as outlined previously [Gil03]), then make moves that stop the opponent
from checkmating you. This article also goes into detail on different heuristics used to guide an A*
search, which is extremely helpful for what we are trying to implement. The paper also discusses
different heuristics for making favorable move sequences for progressive chess (where each player gets
to play an increasing number of moves at a time), but this information is not as applicable for our
project since we will just be focusing on regular chess. There were also heuristics used specifically for
chess endgames. It should also be noted that this reference talked about combining algorithms to keep
the computations more simple. Even though this article was written specifically for progressive chess,
most of the concepts such as using the “ghost” checkmate heuristic can be applied to our project.[JG16]

### 3.2 Search Algorithm Exploration

Search algorithms are a significant part of the design of general chess playing artificial intelligence.
The most simplistic application of a non-trivial search algorithm has to be a brute force search of the
move tree that doesn’t prune or choose paths with any intelligent heuristic [Gil03]. Needless to say,
this is very slow and inefficient, however it is often used as a baseline benchmark for more complex and
intelligent algorithms [Gil03]. However, newer methods that build on top of a naive tree search include
min-max algorithm, alpha-beta pruning, and algorithms that attempt to slim down the representation
of the search tree itself.

The min-max algorithm is a multi-step backtracking algorithm used to locate optimal moves and
paths for players, and is the core of standard chess-playing algorithms. In the min-max algorithm,
two actors (a minimizer and a maximizer) attempt to drive the score to the minimal (minimizer) and
maximal (maximizer) values. At every depth of the tree, every possible move is analyzed and the
resultant scores propagated up the tree. The minimizer and maximizer will select from these scores
based on their heuristic objective (minimum and maximum scores, respectively). Alpha-beta pruning
is an optimization algorithm that builds on the previously described mix-max algorithm, minimizing
the size of the search space. Pruning is accomplished by identifying the scores of every possible move
and completely avoiding branches with worse results. This allows the program to search greater depths
without increasing the required search time. Applying Alpha-Beta pruning can be applied [WBP17]
in code using the point system previously mentioned.[Gil03]


Another method of tree-search starts before the actual tree search and instead uses more effec-
tive representations of the discovery tree so that there are exponentially less branches.[Ber74] From
these search algorithms, we can generally see that the lower the branching factor, the more compute
power can be devoted towards depth; CAPS-II, a chess program from the 1970s, achieved a branching
factor of 1.5 to 3.0 which allowed it to explore much more deeply than other programs of its time.[Ber74]

### 3.3 Further Improvements Made by Previous Chess Algorithms

Chess is studied as three sections made up of the opening, mid-game, and endgame. While some
chess programs have tried to treat all three the same, there have been observations that they have to
use different strategies in order to be successful.[Ber74] For example, the opening moves in chess are
highly standardized and even memorized by chess players because there are a finite number of ”opti-
mal” moves according to opening theory. One paper suggests the use of a ”opening move database”
that simply stores all of the popular opening moves and their best counters because there are a finite
number of them.[WCYH12] By doing this, the chess program could accurately identify the opponent’s
opening pattern and effectively respond with shorter search times by not having to build a search tree
[WCYH12]. The mid-game would utilize most of the aforementioned algorithms and strategies such as
Alpha-Beta Pruning [WBP17], points, and search trees. Much like the opening, the late game can be
handled differently than the middle of each game. The endgame differs from the early game since the
board is so sparse. One typical approach for endgames is to use premade ”endgame tables” [BTH05]
to determine if an endgame situation is even winnable. One key metric is the DTZ50 value, which
represents positions that are winnable within 50 moves against an opponent making the best possible
moves. ”Nalimov’s endgame tables for Western Chess” is a common set of tables that are used, but
there exist other more accurate endgame tables that we can make us of for our project [BTH05]. Other
approaches to analyzing the endgame include looking at specific piece combinations. Some popular
ones to analyze are King and Pawn against King, as well as King and Rook against King.[Bra80]
These endgames with limited piece availability opens up a far less number of positions that the search
tree has to account for (there are only 19 moves needed to win any King and Pawn against King
endgame).[Bra80] Additionally, endgames with limited pieces make the goal heuristic very different;
for example, with a King and Pawn against King endgame, the strategy is to simply move as close to
the enemy pawn as possible in hopes of capturing it.[Bra80] This makes it clear that in the endgame,
we can no longer evaluate the board on points resulting from capture alone.

Even after all of the evaluation and search, there are still uncertainties in chess that can never
be fully predicted. The opponent’s move for example might be completely different from the optimal
ones predicted by a chess program. Alpha-beta pruning, for example, completely ignores any uncer-
tainty in the position of a board.[Hor90] Oftentimes, the board evaluator will not perfectly evaluate
the board and this introduces uncertainty into the program. One approach was the chess program
”Merlin” which took into account a dynamic score in addition to the static score calculated by other
chess evaluators. This allowed it to consider things like passed pawns and king attacks.[Hor90]

```
Besides accounting for the nuances of chess in the opening, mid-game, endgame, and accounting for
```

the uncertainty inherent in any static evaluator, other attempts to further improve chess programs have
included incorporating Bayesian networks and the use of genetic or evolutionary algorithms. Bayesian
networks allowed a chess program to adapt its strategy and evaluation function to its game opponent
and use its playing experience.[FS07] Besides Bayesian networks, many other improvements featuring
learning over multiple games exist and are being explored today. Similar to how Bayesian networks
improve the evaluator, genetic algorithms also learn over iterations and evolves the evaluator function
over time.[TM10] In addition to improving evaluator functions, genetic algorithms have also been used
to tune the search parameters of chess programs and endgames.[LSLD06] Genetic algorithms are fairly
new and have been shown to be very effective even over the best human players. [VFCT11]

### 3.4 Summary of Reviewed Approaches

The existing literature in the field of chess algorithms and strategies has allowed us to focus the
scope of our project on making the most effective chess solver we can with limited time. Reading
through all the existing strategies has given us insight on what methods will be the most effective
for completing our project. The key features we would like to implement are a working evaluator
with search algorithms. Ideally, we will have multiple search algorithms so that the evaluator can mix
and match search strategies based on testing that we perform. As mentioned before, using composite
search algorithms that fuse the results of multiple searches will potentially allow for a higher performing
evaluator. If time allows, we will implement phase-of-game based strategies specifically tailored for the
early or late game. Other strategies in the ”Further Improvements” section will also be added if time
allows. This literature review has allowed us to gather crucial information to complete our project
successfully.

## 4 Approach & Method

We wrote a series of evaluators that incorporate many of the previously mentioned principles, such
as considering captures, checks, and checkmates separately.[Gil03] These evaluators all produce a score
for the board with negative scores representing black advantage and positive scores representing white
advantage. With the multitude of evaluation criteria examined, the evaluator scores were all combined
to make a final decision on which board states were most advantageous to which player. Scores from
individual evaluators are squeezed to be between 0 and 1. The scores are then have a weight applied
to it. For the search portion of our chess engine, we chose to implement Alpha-Beta pruning instead
of A* or a different search algorithm due to the suitability for a 2-person game and the advantage of
keeping the search space smaller via branch pruning.

For our project, we used an existing chess API by Andrea Mostosi[Mos18] to take advantage of
the Alpha-Beta pruning algorithm for our move searcher[WBP17]. For selecting the best move, we
used the evaluators described above to determine the board state for possible board configurations ”n”
turns in the future. Each turn consisted of a move from white and a move from black.

### 4.1 Capture Evaluator

The capture evaluator assigns a point value to a board state based on all legal captures on the
board by adding up their value. The rationale behind this is that a board state in which you can make
lots of captures is desirable.


```
Algorithm 1:Capture Evaluator
1 function Evaluate(Board)
Input :Boardboard
Output:boardvalue
2 boardvalue← 0
3 formoveinboard.legalmovesdo
4 ifmove is capturethen
5 boardvalue +=capturedpiece.value
6 else
7 go to next move
8 end
9 end
```
### 4.2 Pointwise Evaluator

The pointwise evaluator scores the board by counting all pieces and their values irregardless of position.

```
Algorithm 2:Pointwise Evaluator
1 function Evaluate(Board)
Input :Boardboard
Output:boardvalue
2 boardvalue← 0
3 forpieceinboard.piecesdo
4 boardvalue +=piece.value
5 end
6 return boardvalue
```
### 4.3 Positional Evaluator

The positional evaluator weighs all pieces on the board based on where they are placed. For exam-
ple, a knight on the edge or the corner of the board is assigned a much lower value than a knight in
the middle of the board where it can control many squares. Below is an example of the square weights
for a white knight.

#### -50 -40 -30 -30 -30 -30 -40 -

#### -40 -20 0 0 0 0 -20 -

#### -30 0 10 15 15 10 0 -

#### -30 5 15 20 20 15 5 -

#### -30 5 15 20 20 15 5 -

#### -30 0 10 15 15 10 0 -

#### -40 -20 0 0 0 0 -20 -

#### -50 -40 -30 -30 -30 -30 -40 -

### 4.4 Check Opportunity Evaluator

Placing an opponent in check is a good way of forcing moves, and so the check opportunity evaluator
gives more weight to moves that put the opponent in check.


```
Algorithm 3:Check Opportunity Evaluator
1 function Evaluate(Board)
Input :Boardboard
Output:boardvalue
2 boardvalue← 0
3 formoveinboard.legalmovesdo
4 ifmove is capturethen
5 boardvalue +=capturedpiece.value
6 else
7 go to next move
8 end
9 end
10 return boardvalue
```
### 4.5 Checkmate Opportunity Evaluator

Checkmate is the objective of the game and should be prioritized over any other capture or posi-
tional advantage. Captures are weighted very heavily and if a checkmate can be executed, then the
evaluator will recommend this move.

```
Algorithm 4:Checkmate Opportunity Evaluator
1 function Evaluate(Board)
Input :Boardboard
Output:boardvalue
2 boardvalue← 0
3 ifboard has checkmatethen
4 ifboard is white turnthen
5 boardvalue +=∞
6 else
7 boardvalue +=−∞
8 end
9 else
10 boardvalue += 0
11 end
12 return boardvalue
```
### 4.6 Pattern Evaluator

The pattern evaluator is used to avoid draws like stalemate, three-fold repetition, and the 50-move
rule. Essentially, we negatively weight a move that causes a draw of any kind because common chess
strategy is to go for a win.


```
Algorithm 5:Pattern Evaluator
1 function Evaluate(Board)
Input :Boardboard
Output:boardvalue
2 boardvalue← 0
3 ifboard.isstalemate or board.isfivefoldrepetition or board.canclaimthreefoldrepetitionthen
4 ifboard is white turnthen
5 boardvalue +=− 1
6 else
7 boardvalue += 1
8 end
9 else
10 boardvalue += 0
11 end
12 return boardvalue
```
### 4.7 Opening Moves Database

In order to provide the chess AI with a more powerful arsenal of opening strategies, a database
of popular opening moves was established. Opening move functions were written for both the white
and black sides of the board. These functions take as an argument the previous move of the opposite
player in order to facilitate counterplays to possible opponent openings. The default style of play is
the King’s gambit opening, which has been a highly popular chess opening for hundreds of years [unk].

This default algorithm dictates that white move its pawn from position e2 to e4, and then develop
its knight and bishop to protect the pawn and project power to the central area of the board very
early on in the game. This strategy enables provides initiative and momentum to white through rapid
expansion and control of the board. If the opponent does not respond in a way that halts the advance,
they will be at a major disadvantage for the rest of the game. As a response, black has been given
a viable defense to this strong opening, developing its own pawn and knight to meet the aggressive
stance taken by white.

The following pseudocode outlines the approach taken by the AI to engage in opening moves:

```
Algorithm 6:Opening Moves Database (white)
1 function BestMove(previousmove)
Input :Stringpreviousmove
Output:bestmove
2 whiteopeningmoves = [...]
3 ifpreviousmove in whiteopeningmovesthen
4 return whiteopeningmoves[previousmovesindex + 1]
5 else
6 return None
7 end
```
```
Algorithm 7:Opening Moves Database (black)
1 function BestMove(previousmove)
Input :Stringpreviousmove
Output:bestmove
2 blackopeningmoves = [...]
3 ifpreviousmoves in blackopeningmovesthen
4 return blackopeningmoves[previousmovesindex + 1]
5 else
6 return None
7 end
```

### 4.8 Alpha Beta Pruning

The Alpha-Beta pruning algorithm was utilized to perform the searching task for our chess engine.
A function was created that took in a board representation, a depth to explore up to, and an evaluator.
The Alpha-Beta pruning function followed the following pseudocode:

```
Algorithm 8:Chess Alpha Beta Pruning Explore
1 function Explore(Board, Depth, Evaluator, Alpha, Beta)
Input :Boardboard, Depthd, Evaluatore, Alphaa, Betab
Output:move
2 ifthere exist board.legalmovesthen
3 ifwhite’s turnthen
4 formove in board.legalmovesdo
5 boardcopy←board
6 add move to boardcopy
7 b = min(b, explore(boardcopy, d - 1, e, a, b))
8 ifb≤athen
9 return b (return b immediately without considering other moves)
10 end
11 return b
12 end
13 else
14 formove in board.legalmovesdo
15 boardcopy←board
16 add move to boardcopy
17 a = max(a, explore(boardcopy, d - 1, e, a, b))
18 ifb≤athen
19 return a (return a immediately without considering other moves)
20 end
21 return a
22 end
23 end
24 else
25 return e.evaluate board
26 end
```
Algorithm 9:Chess Alpha Beta Pruning
1 function ABP(Board, Depth, Evaluator)
Input :Boardboard, Depthdepth, Evaluatorevaluator
Output:move
2 possibleboards←[]
3 formoveinboard.legalmovesdo
4 boardcopy←board
5 add move to boardcopy
6 boardscore, move←explore(boardcopy)
7 add (boardscore, move) to possibleboards
8 end
9 return move with highest associated boardscore
In this algorithm, the search space is explored recursively. Pruning is enforced in lines 8 through 10
and 18 through 20 in Algorithm 8. For a given search tree, the current move is immediately returned
on line 9 if the black player’s best outcome (form that tree) is worse than their current best possible
outcome. On line 19, the current move is immediately returned if the white player’s best outcome
(form that tree) is worse than their current best possible outcome.

## 8 Contributions

### 8.1 Ambrose Dukek

Researched chess opening strategies and implemented the opening moves database. Ran tests on
the chess AI and collected data relevant to the experimental section of the paper. Assisted with the
creation of the chess search algorithm and stockfish implementation on a personal machine rather than
Google Colab.

### 8.2 Luke Chen

Read and wrote on ”The Technology Chess Program”, ”Chess as Problem Solving: The Develop-
ment of a Tactics Analyzer”, ”BayesChess: A Computer Chess Program Based on Bayesian Networks”,
”Pattern-based Representations of Knowledge in the Game of Chess”, and ”Reasoning with Uncer-
tainty in Computer Chess”.


Created the ensemble of evaluators including a positional evaluator, material evaluator, and a cap-
ture evaluator and wrote a deep analysis on the algorithms behind them in the methods section.
Implemented alpha-beta pruning, breadth first search, and breadth first search with a horizon.

### 8.3 Mathias (Matt) Martinez-Zamora

Worked on getting the search algorithm portion of the chess AI working. Tested different methods
of implementing visuals for the board representation and other chess engines to test our AI against.
Worked on Stockfish integration for google collab and running the code on a personal machine.


## References

[Ber74] Hans J. Berliner. Chess as problem solving: The development of a tactics analyzer. Com-
puter Science Department Carnegie-Mellon University Pittsburgh, Pennsylvania, USA,
1974.

[BGCE90] Hans J. Berliner, Gordon Goetsch, Murray S. Campbell, and Carl Ebeling. Measuring the
performance potential of chess programs.Artificial Intelligence, 43(1):7–20, 1990.

[Bra80] M. A. Bramer. Pattern-based representations of knowledge in the game of chess. Technical
report, Mathematics Faculty, Open University, Milton Keynes MK7 6AA, U.K., 1980.

[BTH05] M.S. Bourzutschky, J.A. Tamplin, and G.McC. Haworth. Chess endgames: 6-man data
and strategy.Theoretical Computer Science, 349(2):140–157, 2005. Advances in Computer
Games.

[FS07] Antonio Fern ́andez and Antonio Salmer ́on. Bayeschess: A computer chess program based
on bayesian networks.Pattern Recognition Letters, 29(8):1154–1159, 2007.

[Gil03] James Gillogly. The technology chess program. Technical report, Carnegie-Mellon Uni-
versity, Department of Computer Science, Pittsburgh, Pennsylvania, USA, 2003.

[Hor90] Helmut Horacek. Reasoning with uncertainty in computer chess. Artificial Intelligence,
Volume 43, Issue 1, pages 37–56, 1990.

[JG16] Vito Janko and Matej Guid. A program for progressive chess. Theoretical Computer
Science, 644:76–91, 2016. Recent Advances in Computer Games.

[LSLD06] Nicolas Lassabe, St ́ephane Sanchez, Herv ́ee Luga, and Yves Duthen. Genetically pro-
grammed strategies for chess endgame. pages 831–838. GECCO ’06: Proceedings of the
8th annual conference on Genetic and evolutionary computation, 2006.

[Mos18] Andrea Mostosi. zenkay/py-chess-api. https://github.com/zenkay/py-chess-api, 8

2018. [Online; accessed Nov-2021].

[TM10] Lothar M. Schmitt Tomohiko Mitsuta. Optimizing the performance of gnu-chess with a ge-
netic algorithm. pages 124–131. HC ’10: Proceedings of the 13th International Conference
on Humans and Computers, 2010.

[unk] unknown. Chess openings.https://www.chess.com/openings.

[VFCT11] Eduardo V ́azquez-Fern ́andez, Carlos Artemio Coello, and Feliu Davino Sagols Troncoso.
An adaptive evolutionary algorithm based on typical chess problems for tuning a chess
evaluation function. page 39–40. GECCO ’11: Proceedings of the 13th annual conference
companion on Genetic and evolutionary computation, 2011.

[WBP17] Lukman Heryawan Werda Buana Putra. Applying alpha-beta algorithm in a chess engine.
Jurnal Teknosains: Jurnal Ilmiah Sains Dan Teknologi, 6(1):37–43, 2017.

[WCYH12] Kuang-Yu Wu, Jr-Chang Chen, Shi-Jim Yen, and Shun-Chin Hsu. Design of knowledge-
based opening database for minishogi. In2012 Conference on Technologies and Applica-
tions of Artificial Intelligence, pages 290–293, 2012.

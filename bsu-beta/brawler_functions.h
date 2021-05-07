#ifndef BRAWLER_FUNC_H
#define BRAWLER_FUNC_H

/* forward declaration(s) */
int powerPointsToLevel(struct brawler_t *);
int powerPointsToMax(struct brawler_t *);
int coinsToLevel(struct brawler_t *);
int coinsToMax(struct brawler_t *);
int calcPowerPointsToLevel(int, int);
int calcPowerPointsCurr(int, int);
int calcPotentialLevel(int, int);
#endif
